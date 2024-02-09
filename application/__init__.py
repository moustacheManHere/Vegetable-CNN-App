from flask import Flask 
from flask_uploads import UploadSet, IMAGES, configure_uploads

app = Flask(__name__)
app.config.from_pyfile("config.cfg")
app.config["UPLOADS_DEFAULT_DEST"] = "application/static/"
app.config["UPLOADED_PHOTOS_DEST"] = "uploads"
app.config["IMAGE_LOCATION"] = "static/uploads"

photos = UploadSet("uploads", IMAGES)
configure_uploads(app, photos)

from application import routes