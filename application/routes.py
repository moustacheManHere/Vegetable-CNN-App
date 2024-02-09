from application import app
from flask import render_template, request, flash, send_from_directory, url_for
from flask import json, jsonify
from application.forms import UploadForm
from application import photos
from application.deeplearning import get_prediction


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
    file_url = None
    form = UploadForm()
    if form.validate_on_submit():
        filename = photos.save(form.photo.data)
        file_url = url_for("get_file", filename= filename)
        response = get_prediction(filename) # later do dynamic size switching function
    else:
        file_url = None
        response = None
    return render_template("predict.html", form = form, file_url=file_url, response = response, vegetable_list=vegetable_list) # try to have a more human response. 

@app.route('/uploads/<filename>')
def get_file(filename):
    return send_from_directory(app.config["IMAGE_LOCATION"], filename)


#@app.errorhandler(Exception)
def handle_error(e):
    error_code = getattr(e, 'code', 500)  
    print(e)
    return render_template('error.html', error_code=error_code), error_code