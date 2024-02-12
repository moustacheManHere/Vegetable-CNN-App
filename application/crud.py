from application import db
from application.models import *
import boto3 
from PIL import Image
import base64
from io import BytesIO
import uuid 
from datetime import datetime, timedelta
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sqlalchemy import case

s3 = boto3.resource("s3")
imgBucket = s3.Bucket("devops-ca2")
vegetable_list = [
    "Broccoli",
    "Capsicum",
    "Bottle_Gourd",
    "Radish",
    "Tomato",
    "Brinjal",
    "Pumpkin",
    "Carrot",
    "Papaya",
    "Cabbage",
    "Bitter_Gourd",
    "Cauliflower",
    "Bean",
    "Cucumber",
    "Potato"
]

def get_all_vegetables(convert= True):
    query = Vegetable.query.all()
    if convert:
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

def remove_hist(id):
    try:
        entry = db.get_or_404(History, id)
        db.session.delete(entry)
        db.session.commit()
    except Exception as error:
        print(error)
        db.session.rollback()
        return 0

def save_to_cloud(img_data):
    # data must be base64

    #get unique filename
    unique_id = uuid.uuid4()
    path = f"usr_img_{unique_id}"

    #check if file exists
    try:
        s3.Object("devops-ca2",path).load()
        unique_id = uuid.uuid4()
        path = f"usr_img_{unique_id}"
    except:
        pass
    
    #upload
    obj = s3.Object("devops-ca2", path)
    obj.put(Body=base64.b64decode(img_data))
    return path

def add_history(id, path, response, comment):
    
    new_hist = History(id=id,vegeID=int(response[0])+1,filename=path,percentage=float(response[1]),comment=comment)
    db.session.add(new_hist)
    db.session.commit()
    return new_hist

def get_all_history(id, convert= True):
    query = History.query.filter_by(id=id).all() 
    if convert:
        for i in query: # later u shld insert logic to convert base64
            i.filename = url_to_b64(i.filename)
    return query

def filter_history(id, form):
    query = History.query.filter_by(id=id)
    
    if form.vegetable.data != "*":
        query = query.filter_by(vegeID=int(form.vegetable.data))

    if form.percentage.data is not None:
        query = query.filter(History.percentage >= form.percentage.data)
    
    if form.date.data != "*":
        start_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        end_date = start_date + timedelta(days=int(form.date.data))
        query = query.filter(History.date >= start_date, History.date < end_date)
    
    if form.query.data not in ["", " ", None]:
        query_order = order_by_text(query, form.query.data)
        ordering = case({id: index for index, id in enumerate(query_order)}, value=History.histID)

        ordered_query = query.order_by(ordering)
        return ordered_query.all()

    return query.all()



def order_by_text(query, user_text):
    batch_size = 10 
    results = []
    query = query.all()
    
    vectorizer = TfidfVectorizer()

    query_tfidf = vectorizer.fit_transform([user_text.lower()])

    for i in range(0, len(query), batch_size):
        batch_comments = [comment.comment.lower() + " "+ vegetable_list[comment.vegeID-1].lower()+ " " + str(comment.percentage) + " " + str(int(comment.percentage)) for comment in query[i:i+batch_size]]
        print(batch_comments)
        tfidf_matrix_batch = vectorizer.transform(batch_comments)

        similarity = cosine_similarity(tfidf_matrix_batch, query_tfidf)

        batch_results = [(query[i+j].histID, similarity[j][0]) for j in range(len(batch_comments))]

        results.extend(batch_results)

    results = sorted(results, key=lambda x: x[1], reverse=True)
    print(results)
    results = [i[0] for i in results]
    return results
