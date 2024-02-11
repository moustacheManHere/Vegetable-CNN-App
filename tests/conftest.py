import pytest
from application import app as application
import os 
import io
from application import create_app
from application.models import populate_vege
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, flash, send_from_directory, url_for
from flask import json, jsonify
from application.forms import UploadForm
from application.deeplearning import get_prediction
from application.crud import *
import base64

class TestAppConfig:
    DEBUG = True
    ENV = 'development'
    SECRET_KEY = 'lmao'
    DL_URL_SMALL = 'https://vegetablecnn-053e.onrender.com/v1/models/small'
    DL_URL_LARGE = 'https://vegetablecnn-053e.onrender.com/v1/models/large'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db_test.db'
    TESTING = True
    WTF_CSRF_ENABLED = False

@pytest.fixture
def app():
    app = create_app(TestAppConfig)

    @app.route('/')
    @app.route('/index')
    @app.route('/home')
    def index_page():
        return render_template("index.html")

    @app.route('/predict',methods=["GET","POST"])
    def predict():
        form = UploadForm()
        if form.validate_on_submit():
            photo = form.photo.data
            image_data = photo.read()
            response = get_prediction(image_data)
            img_64 = base64.b64encode(image_data).decode('utf-8')
        else:
            print(form.errors)
            img_64 = None
            response = None
        vegetable_list = [
    "Bean",
    "Bitter_Gourd",
    "Bottle_Gourd",
    "Brinjal",
    "Broccoli",
    "Cabbage",
    "Capsicum",
    "Carrot",
    "Cauliflower",
    "Cucumber",
    "Papaya",
    "Potato",
    "Pumpkin",
    "Radish",
    "Tomato"
]

        return render_template("predict.html", form = form, img_64=img_64, response = response, vegetable_list=vegetable_list) # try to have a more human response. 

    @app.route('/veges')
    def vege_page():
        try: 
            print("veges")
            veges = get_all_vegetables()
            
            print(veges)
        except:
            raise ValueError() 
        
        return render_template("catalogue.html", items=veges)

    @app.route('/info/<id>')
    def vege_info(id):
        try: 
            print("veges")
            vege = get_one_vegetable(id)
            
            print(vege[0])
        except:
            raise ValueError() 
        
        return render_template("info.html", vegetable=vege[0])


    @app.errorhandler(Exception)
    def handle_error(e):
        error_code = getattr(e, 'code', 500)  
        print(e)
        return render_template('error.html', error_code=error_code), error_code
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def db(app):
    db = SQLAlchemy(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
        populate_vege(db)
        db.session.commit()
    yield db
    db.drop_all()

@pytest.fixture
def test_image():
    image_path = "application/static/images/0001.jpg"
    with open(image_path, 'rb') as f:
        return io.BytesIO(f.read())