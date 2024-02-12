from application import db
from datetime import datetime
from flask_login import UserMixin
import pandas as pd

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

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

class History(db.Model):
    histID = db.Column(db.Integer, primary_key=True, nullable=False)
    id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    vegeID = db.Column(db.Integer, db.ForeignKey("vegetable.id"), nullable=False)
    filename = db.Column(db.String(50), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)  
    percentage = db.Column(db.Float, nullable=True)
    comment = db.Column(db.Text, nullable=True)

    def __init__(self, id, vegeID, filename, percentage=None, comment=None):
        self.id = id
        self.vegeID = vegeID
        self.filename = filename
        self.percentage = percentage
        self.comment = comment

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
