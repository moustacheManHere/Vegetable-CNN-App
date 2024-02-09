from application import app
from flask import render_template, request, flash, send_from_directory, url_for
from flask import json, jsonify
from application.forms import UploadForm
from application import photos

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
    else:
        file_url = None
    return render_template("predict.html", form = form, file_url=file_url)

@app.route('/uploads/<filename>')
def get_file(filename):
    return send_from_directory("static/uploads", filename)


#@app.errorhandler(Exception)
def handle_error(e):
    error_code = getattr(e, 'code', 500)  
    print(e)
    return render_template('error.html', error_code=error_code), error_code