from application import app
from flask import render_template, request, flash
from flask import json, jsonify

@app.route('/')
@app.route('/index')
@app.route('/home')
def index_page():
    return render_template("index.html")
