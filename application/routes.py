from application import app
from flask import render_template, abort, redirect, url_for
from flask_login import current_user,login_required, logout_user
from application.forms import *
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

@app.route("/history", methods=["GET", "POST"])
def history():
    form = SearchForm()
    if form.validate_on_submit():
        print("lol")
    return render_template("history.html",form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    login = LoginForm()
    if login.validate_on_submit():
        if checkUserCred(login):
            return redirect(url_for("index_page"))
        return render_template("login.html", title="Login", form=login)
    return render_template("login.html", title="Login", form=login)

@app.route("/signup", methods=["GET", "POST"])
def signup():
    signup = SignupForm()
    if signup.validate_on_submit():
        add_user(signup)
        return redirect(url_for("index_page"))
    return render_template("signup.html", title="Signup", form=signup)

@app.route("/profile", methods=["GET", "POST"])
def profile():
    if not current_user.is_authenticated:
        abort(401)
    profForm = UpdateProfileForm()
    if profForm.validate_on_submit():
        updateProfile(current_user.get_id(), profForm)
        return redirect(url_for("profile"))
    return render_template("profile.html", title="Profile", form=profForm)

@app.route("/unauthorised")
def test_unauth_page():
    # abort(401) to call this error. 
    return render_template('unauthorized.html', error_code=401)

@app.route("/logout")
def logout():
    if not current_user.is_authenticated:
        abort(401)
    logout_user()
    return redirect(url_for("index_page"))

@app.errorhandler(Exception)
def handle_error(e):
    error_code = getattr(e, 'code', 500)  
    print(e)
    if error_code == 401:
        return render_template('unauthorized.html', error_code=error_code), error_code
    return render_template('error.html', error_code=error_code), error_code