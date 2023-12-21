import pandas as pd
from spk_model import WeightedProduct

class BigBike():

    def __init__(self) -> None:
        self.bigbike = pd.read_csv('SPK_Syahdan.csv')

    def get_recs(self, kriteria):
        wp = WeightedProduct(self.bigbike.to_dict(orient="records"), kriteria)
        return wp.calculate
