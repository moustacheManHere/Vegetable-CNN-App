from application.forms import * 
from bs4 import BeautifulSoup
from flask import url_for
from application.models import *

def test_vegetable_database_add(db):
    assert db.session.query(Vegetable).count() == 15
    new_vegetable = Vegetable(name='Test Vegetable', filename='test_filename.jpg', 
                              short='Short description', description='Description of the vegetable')
    db.session.add(new_vegetable)
    db.session.commit()
    assert db.session.query(Vegetable).count() == 16

def test_vegetable_database_query(db):
    vegetable = db.session.query(Vegetable).first()
    assert vegetable is not None
    assert vegetable.name == "Bean" 
    assert vegetable.filename == 'vgdb_01.jpg'

    vegetable = db.session.query(Vegetable).order_by(Vegetable.id.desc()).first()
    assert vegetable is not None
    assert vegetable.name == "Tomato"
    assert vegetable.filename == 'vgdb_15.jpg'


def test_predict_route(client,app, test_image):
    with app.test_request_context():
        response = client.post(
            url_for('predict'),
            data={'photo': (test_image, 'test.png')},
            content_type='multipart/form-data'
        )
    assert response.status_code == 200

    # check html to see if success
    soup = BeautifulSoup(response.data, 'html.parser')
    result_message = soup.find('h3', class_='mt-3').get_text(strip=True)
    assert "I'm" in result_message