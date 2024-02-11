from application import app
from flask import render_template
from flask_login import current_user
from application.forms import UploadForm
from application.deeplearning import get_prediction
from application.crud import *
from application.auth import *
import base64

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