from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import (
    SubmitField,
    StringField,
    PasswordField,
    FileField,
    TextAreaField,
    SelectField,
    FloatField
)
from wtforms.validators import (
    Optional,
    DataRequired,
    Length,
    EqualTo,
    InputRequired,
    NumberRange,
    Optional,
    ValidationError
)
from flask_uploads import IMAGES
from application import app
from application.models import Vegetable


class UploadForm(FlaskForm):
    photo = FileField(validators=[
        FileAllowed(("jpg","jpeg"), "Only jpg/jpeg images allowed!"), # checking file extension here
        FileRequired("Must have one file!")
    ])
    comments = TextAreaField("Comments") 

    submit = SubmitField("Upload")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    submit = SubmitField("Login")


class SignupForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Sign Up")


class UpdateProfileForm(FlaskForm):
    name = StringField("Name", validators=[Optional()])
    new_password = PasswordField("New Password", validators=[Optional(), Length(min=6)])
    submit = SubmitField("Update Profile")

# Init Vegetable Choices
with app.app_context():
    all_veges = query = Vegetable.query.all()
vegetables = [("*","All")] + [(i.id,i.name.replace("_"," ")) for i in all_veges]

class SearchForm(FlaskForm):
    vegetable = SelectField('Prediction', choices=vegetables, validators=[InputRequired()])

    query = StringField("Magic Query", validators=[Optional(), Length(max=50)])

    date_choices = [(1, '1 Day Back'), (7, '7 Days Back'), (30, '30 Days Back'), ("*", "All")]
    date = SelectField('Date', choices=date_choices, validators=[InputRequired()])

    percentage = FloatField('Minimum %', validators=[Optional(),NumberRange(min=0, max=101, message='Must be between 0 and 100')])

    submit = SubmitField('Search')