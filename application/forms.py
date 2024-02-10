from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import (
    SubmitField,
    FileField
)
from wtforms.validators import (
    InputRequired
)
from flask_uploads import IMAGES

class UploadForm(FlaskForm):
    photo = FileField(validators=[
        FileAllowed(IMAGES, "Only images allowed!"), # checking file extension here
        FileRequired("Must have one file!")
    ])

    submit = SubmitField("Upload")