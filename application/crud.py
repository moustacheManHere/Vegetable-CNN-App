from application import db
from application.models import *

def get_all_vegetables():
    query = Vegetable.query.all()
    for i in query: # later u shld insert logic to convert base64
        i.filename = "lol.txt"
        #print(i.filename)
    return query