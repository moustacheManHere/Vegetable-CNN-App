from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import (
    SubmitField,
    StringField,
    PasswordField,
    FileField
)
from wtforms.validators import (
    Optional,
    DataRequired,
    Length,
    EqualTo,
)
from flask_uploads import IMAGES

class UploadForm(FlaskForm):
    photo = FileField(validators=[
        FileAllowed(IMAGES, "Only images allowed!"), # checking file extension here
        FileRequired("Must have one file!")
    ])

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