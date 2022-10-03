from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
import time
import json
from services.api.utils.functions import file_to_json

app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)
api = Api(app)


def make_results(results):
    result_data = []
    for result in results:
        result_dict = {'date': result.date, 'open': result.open, 'high': result.high,
                       'low': result.low, 'close': result.close, 'adj_close': result.adj_close,
                       'volume': result.volume}
        result_data.append(result_dict)
        del result_dict
    return result_data


class Errors:
    def return_error(self, code, description=None):
        if code == 400:
            description = 'Bad Request'
        elif code == 401:
            description = 'Unauthorized'
        mess = {'Result': False, 'Description': description, 'Code': code, 'ContentType': 'application/json'}
        return json.dumps(mess)


class Data(db.Model):
    """таблица данных"""

    __tablename__ = 'Data'
    id = db.Column(db.Integer(), primary_key=True)
    date = db.Column(db.Date, nullable=False, default=time.strftime("%Y-%m-%d", time.localtime()))
    open = db.Column(db.Float(), nullable=False)
    high = db.Column(db.Float(), nullable=False)
    low = db.Column(db.Float(), nullable=False)
    close = db.Column(db.Float(), nullable=False)
    adj_close = db.Column(db.Float(), nullable=False)
    volume = db.Column(db.Float(), nullable=False)

    def __repr__(self):
        return str(Data.__dict__)

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    @classmethod
    def update_orders(cls):
        orders_entries = []
        for orders in file_to_json('data/aapl.csv'):
            try:
                new_entry = Data(**orders)
                orders_entries.append(new_entry)
            except Exception as e:
                print(e)
        db.session.add_all(orders_entries)
        db.session.commit()

    @classmethod
    def find_by_two_date(cls, date_before, date_after):
        return cls.query.filter(Data.date <= date_before, Data.date >= date_after).all()

    @classmethod
    def find_by_before_date(cls, date_before):
        return cls.query.filter(Data.date < date_before).all()

    @classmethod
    def find_by_after_date(cls, date_after):
        return cls.query.filter(Data.date > date_after).all()


class Getdata(Resource, Errors):
    """эндпоинт для  получения данных """
    def post(self):
        try:
            _json = request.get_json(force=True)
            date_before = _json.get('date_before')
            date_after = _json.get('date_after')
            if date_before and date_after:
                try:
                    result_data = make_results(Data.find_by_two_date(date_before, date_after))
                except:
                    return Errors.return_error(self, 400)
            elif date_before and not date_after:
                try:
                    result_data = make_results(Data.find_by_before_date(date_before))
                except:
                    return Errors.return_error(self, 400)
            elif not date_before and date_after:
                try:
                    result_data = make_results(Data.find_by_after_date(date_after))
                except:
                    return Errors.return_error(self, 400)
            else:
                return Errors.return_error(self, 400)
        except:
            return Errors.return_error(self, 400)
        return json.dumps(result_data, default=str)


class Adddata(Resource, Errors):
    """эндпоинт для заливки таблицы данных"""
    def get(self):
        Data.update_orders()
        return {'Result': True, 'Description': 'done', 'Code': 200, 'ContentType': 'application/json'}


api.add_resource(Getdata, '/get_data')
api.add_resource(Adddata, '/add_data')


@app.route("/")
def check_started():
    return jsonify(api="started")
