from application import db
from application.models import *
import boto3 
from PIL import Image
import base64
from io import BytesIO

s3 = boto3.resource("s3")
imgBucket = s3.Bucket("devops-ca2")

def get_all_vegetables():
    query = Vegetable.query.all()
    for i in query: # later u shld insert logic to convert base64
        i.filename = url_to_b64(i.filename)
    return query

def get_one_vegetable(id):
    query = Vegetable.query.filter_by(id=id).all()
    query[0].filename = url_to_b64(query[0].filename)
    return query

def url_to_b64(url):
    img = imgBucket.Object(url)
    resp = img.get()
    file_stream = resp["Body"]
    im = Image.open(file_stream)

    with BytesIO() as buffer:
        im.save(buffer, format="JPEG")  # You can specify the desired image format here
        base64_image = base64.b64encode(buffer.getvalue()).decode()
    
    return "data:image/jpeg;charset=utf-8;base64,"+base64_image