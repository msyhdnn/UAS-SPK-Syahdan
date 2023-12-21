from http import HTTPStatus

from flask import Flask, request
from flask_restful import Resource, Api 

from models import BigBike

app = Flask(__name__)
api = Api(app)        

class Recommendation(Resource):

    def post(self):
        criteria = request.get_json()
        valid_criteria = ['Nama','Harga','cc','full_tank','Daya_KW','Torsi_Max']
        bigbike = BigBike()

        if not criteria:
            return 'criteria is empty', HTTPStatus.BAD_REQUEST.value

        if not all([v in valid_criteria for v in criteria]):
            return 'criteria is not found', HTTPStatus.NOT_FOUND.value

        recommendations = bigbike.get_recs(criteria)

        return {
            'alternatif': recommendations
        }, HTTPStatus.OK.value


api.add_resource(Recommendation, '/recommendation')

if __name__ == '__main__':
    app.run(port='5005', debug=True)
