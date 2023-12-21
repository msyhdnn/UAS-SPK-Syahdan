import sys

from colorama import Fore, Style
from models import Base, BigBike
from engine import engine

from sqlalchemy import select
from sqlalchemy.orm import Session
from settings import BIKE_SCALE

session = Session(engine)

def create_table():
    Base.metadata.create_all(engine)
    print(f'{Fore.GREEN}[Success]: {Style.RESET_ALL}Database has created!')

class BaseMethod():

    def __init__(self):
        # 1-6 (Kriteria)
        self.raw_weight = {
            'Nama': 4,
            'Harga': 5,
            'cc': 6,
            'full_tank': 3,
            'Daya_KW': 1,
            'Torsi_Max': 2
        }

    @property
    def weight(self):
        total_weight = sum(self.raw_weight.values())
        return {c: round(w/total_weight, 2) for c,w in self.raw_weight.items()}

    @property
    def data(self):
        query = select(BigBike)
        return [{
            'id': bigbike.Nama,
            'Nama': BIKE_SCALE[bigbike.Nama],
            'Harga': bigbike.Harga,
            'cc': bigbike.cc,
            'full_tank': bigbike.full_tank,
            'Daya_KW': bigbike.Daya_KW,
            'Torsi_Max': bigbike.Torsi_Max
        } for bigbike in session.scalars(query)]

    @property
    def normalized_data(self):
        # x/max [benefit]
        # min/x [cost]

        Nama = [] # max
        Harga = [] # min
        cc = [] # max
        full_tank = [] # max
        Daya_KW = [] # max
        Torsi_Max = [] # max

        for data in self.data:
            Nama.append(data['Nama'])
            Harga.append(data['Harga'])
            cc.append(data['cc'])
            full_tank.append(data['full_tank'])
            Daya_KW.append(data['Daya_KW'])
            Torsi_Max.append(data['Torsi_Max'])

        max_Nama = max(Nama)
        min_Harga = min(Harga)
        max_cc = max(cc)
        max_full_tank = max(full_tank)
        max_Daya_KW = max(Daya_KW)
        max_Torsi_Max = max(Torsi_Max)

        return [{
            'id': data['id'],
            'Nama': data['Nama']/max_Nama, # benefit
            'Harga': min_Harga/data['Harga'], # cost
            'cc': data['cc']/max_cc, # benefit
            'full_tank': data['full_tank']/max_full_tank, # benefit
            'Daya_KW': data['Daya_KW']/max_Daya_KW, # benefit
            'Torsi_Max': data['Torsi_Max']/max_Torsi_Max # benefit
        } for data in self.data]
 
class WeightedProduct(BaseMethod):
    @property
    def calculate(self):
        weight = self.weight
        # calculate data and weight[WP]
        result = {row['id']:
            round(
                row['Nama'] ** weight['Nama'] *
                row['Harga'] ** (-weight['Harga']) *
                row['cc'] ** weight['cc'] *
                row['full_tank'] ** weight['full_tank'] *
                row['Daya_KW'] ** weight['Daya_KW'] *
                row['Torsi_Max'] ** weight['Torsi_Max']
                , 2
            )

            for row in self.normalized_data}
        #sorting
        # return result
        return dict(sorted(result.items(), key=lambda x:x[1]))

class SimpleAdditiveWeighting(BaseMethod):
    
    @property
    def calculate(self):
        weight = self.weight
        # calculate data and weight
        result = {row['id']:
            round(
                row['Nama'] * weight['Nama'] +
                row['Harga'] * weight['Harga'] +
                row['cc'] * weight['cc'] +
                row['full_tank'] * weight['full_tank'] +
                row['Daya_KW'] * weight['Daya_KW'] +
                row['Torsi_Max'] * weight['Torsi_Max']
                , 2
            )
            for row in self.normalized_data
        }
        # sorting
        return dict(sorted(result.items(), key=lambda x:x[1]))

def run_saw():
    saw = SimpleAdditiveWeighting()
    print('result:', saw.calculate)

def run_wp():
    wp = WeightedProduct()
    print('result:', wp.calculate)

if len(sys.argv)>1:
    arg = sys.argv[1]

    if arg == 'create_table':
        create_table()
    elif arg == 'saw':
        run_saw()
    elif arg =='wp':
        run_wp()
    else:
        print('command not found')
