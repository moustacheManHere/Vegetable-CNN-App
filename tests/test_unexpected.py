from application.forms import * 
from bs4 import BeautifulSoup
from flask import url_for
from application.models import *
from flask_login import current_user
from application.auth import checkUserCred

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
    assert vegetable.name == "Broccoli" 
    assert vegetable.filename == 'vgdb_05.jpg'

    vegetable = db.session.query(Vegetable).order_by(Vegetable.id.desc()).first()
    assert vegetable is not None
    assert vegetable.name == "Potato"
    assert vegetable.filename == 'vgdb_12.jpg'

def test_user_add_remove(db):
    test_user = User(name='Test User', email='test2@example.com', password='password')
    db.session.add(test_user)
    db.session.commit()
    retrieved_user = User.query.filter_by(id=test_user.id).first()

    assert retrieved_user is not None
    assert retrieved_user.name == 'Test User'
    assert retrieved_user.email == 'test2@example.com'
    assert retrieved_user.password == 'password'

    entry = db.get_or_404(User, test_user.id)
    db.session.delete(entry)
    db.session.commit()
    
    retrieved_user = User.query.filter_by(id=test_user.id).first()
    assert retrieved_user is None

def test_check_login(db, app):
    with app.test_request_context():
        valid_login_form = LoginForm(email='default@example.com', password='password')
        result = checkUserCred(valid_login_form)
        assert result is True
        assert current_user.is_authenticated
        assert current_user.name == 'default_user'
        assert current_user.email == 'default@example.com'

def test_predict_route(client,app, test_image):
    with app.test_request_context():
        response = client.post(
            url_for('predict'),
            data={'photo': (test_image, 'test.jpg')},
            content_type='multipart/form-data'
        )
    assert response.status_code == 200

    # check html to see if success
    soup = BeautifulSoup(response.data, 'html.parser')
    result_message = soup.find('h3', class_='mt-3').get_text(strip=True)
    assert "I'm" in result_message

def test_history_add_remove(app, db):
    with app.test_request_context("/history"):


        history_entry = History(
            id=1,
            vegeID=1,  
            filename="test_image.jpg",
            percentage=0.75,  
            comment="Test comment"
        )

        # Add the history entry to the database and check
        db.session.add(history_entry)
        db.session.commit()
        assert history_entry.histID is not None

        # Retrieve the history entry from the database and ensure consistency
        retrieved_entry = History.query.filter_by(histID=history_entry.histID).first()
        assert retrieved_entry is not None
        assert retrieved_entry.id == 1
        assert retrieved_entry.vegeID == 1  
        assert retrieved_entry.filename == "test_image.jpg"
        assert retrieved_entry.percentage == 0.75
        assert retrieved_entry.comment == "Test comment"

        # Remove the history entry from the database
        db.session.delete(retrieved_entry)
        db.session.commit()
        assert History.query.filter_by(histID=retrieved_entry.histID).first() is None
