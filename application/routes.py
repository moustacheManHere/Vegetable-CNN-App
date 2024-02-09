from application import app
from flask import render_template, request, flash
from flask import json, jsonify

@app.route('/')
@app.route('/index')
@app.route('/home')
def index_page():
    return render_template("index.html")

@app.errorhandler(Exception)
def handle_error(e):
    error_code = getattr(e, 'code', 500)  
    return render_template('error.html', error_code=error_code), error_code