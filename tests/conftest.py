import pytest
from application import app as application

@pytest.fixture
def app():
    yield application

@pytest.fixture
def client(app):
    return app.test_client()

