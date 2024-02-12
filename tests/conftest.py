import pytest
from application import app as application
from application import db as database
import os 
import io
from application.models import populate_vege, User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()

@pytest.fixture
def app():
    yield application

@pytest.fixture
def client(app):
    app.config['WTF_CSRF_ENABLED'] = False
    return app.test_client()

@pytest.fixture
def test_image():
    image_path = "application/static/images/0001.jpg"
    with open(image_path, 'rb') as f:
        return io.BytesIO(f.read())

@pytest.fixture
def db(app):
    with app.app_context():
        database.create_all()
        populate_vege(database)
        password = bcrypt.generate_password_hash('password')
        user = User(name='default_user', email='default@example.com', password=password)
        database.session.add(user)
        database.session.commit()
        yield database
        database.drop_all()
