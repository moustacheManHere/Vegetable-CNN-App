from application import db
from datetime import datetime
import pandas as pd


from application import db
from datetime import datetime
import pandas as pd


class Vegetable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    filename = db.Column(db.String(50), nullable=False)
    short = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __init__(self, name, filename, description, short):
        self.name = name
        self.filename = filename
        self.short = short
        self.description = description

def populate_vege(db):
    if Vegetable.query.count() ==  0:
        try:
            df = pd.read_csv("./application/static/vegeDB.csv")
            data_to_insert = df.to_dict(orient="records")
            db.session.bulk_insert_mappings(Vegetable, data_to_insert)
            db.session.commit()
            print("Vegetable data has been successfully populated.")
        except Exception as e:
            db.session.rollback()
            print(f"Error while populating vegetable data: {str(e)}")
    pass


def populate_vege():
    if Vegetable.query.count() ==  0:
        try:
            df = pd.read_csv("./application/static/vegeDB.csv")
            data_to_insert = df.to_dict(orient="records")
            db.session.bulk_insert_mappings(Vegetable, data_to_insert)
            db.session.commit()
            print("Vegetable data has been successfully populated.")
        except Exception as e:
            db.session.rollback()
            print(f"Error while populating vegetable data: {str(e)}")
    pass
