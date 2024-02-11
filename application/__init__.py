from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile("config.cfg")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy()

with app.app_context():
    db.init_app(app)

    from .models import *

    db.create_all()
    populate_vege()
    db.session.commit()
    print("Created Database!")

from application import routes



def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)  # Initialize SQLAlchemy with the app

    from application import routes  # Import routes here to avoid circular import

    return app