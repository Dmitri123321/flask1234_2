from flask.cli import FlaskGroup
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from utils.functions import *
from project import app, db, Data


cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    orders_entries = []
    for orders in file_to_json('resources/aapl.csv'):
        try:
            new_entry = Data(**orders)
            orders_entries.append(new_entry)
        except Exception as e:
            print(e)
    db.session.add_all(orders_entries)
    db.session.commit()


if __name__ == "__main__":
    cli()
