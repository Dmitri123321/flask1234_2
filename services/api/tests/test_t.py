from pprint import pprint
import json, sys, os
import pytest

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
# from werkzeug.test import Client
# from werkzeug.testapp import test_app
from ..project import app


@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client


def test_two_dates(client):
    json_ = {'date_before': '2014-10-29', 'date_after': '2014-10-21'}
    res = client.post('/get_data', json=json_)
    assert res.status_code == 200
    assert type(json.loads(res.json)) == dict


def test_date_before(client):
    json_ = {'date_before': '2014-10-29'}
    res = client.post('/get_data', json=json_)

    assert res.status_code == 200
    assert type(json.loads(res.json)) == dict


def test_date_after(client):
    json_ = {'date_after': '2014-10-21'}
    res = client.post('/get_data', json=json_)

    assert res.status_code == 200
    assert type(json.loads(res.json)) == dict
