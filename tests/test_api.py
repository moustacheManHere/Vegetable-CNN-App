import pytest 
from application.models import *
from application.auth import checkUserCred
from application.forms import * 

@pytest.mark.parametrize("route", ['/', '/index', '/home'])
def test_index_page(client, route):
    response = client.get(route)
    assert response.status_code == 200

@pytest.mark.parametrize("vegetable_id", list(range(1, 16)))
def test_info_page_get(client, vegetable_id, app):
    with app.test_request_context("/info"):
        response = client.get(f'/info/{vegetable_id}')
        assert response.status_code == 200
        assert b"Vegetable Details" in response.data

def test_predict_page_get(client):
    response = client.get('/predict')
    assert response.status_code == 200

def test_error_handler(client):
    response = client.get('/lmao')
    assert response.status_code == 404

def test_veges_page_get(client):
    response = client.get('/veges')
    assert response.status_code == 200
    assert b"Tommy's Friends" in response.data
    assert b"Bitter_Gourd" in response.data

def test_veges_page_get(client):
    response = client.get('/login')
    assert response.status_code == 200
    assert b"Password" in response.data
    assert b"Name" not in response.data

def test_hist_page_get(client, app, db):
    with app.test_request_context():
        response = client.get('/history')
        assert response.status_code == 401
        valid_login_form = LoginForm(email='default@example.com', password='password')
        result = checkUserCred(valid_login_form)
        response = client.get('/profile')
        assert response.status_code == 200

def test_prof_page_get(client, db, app):
    with app.test_request_context("/profile"):
        response = client.get('/profile')
        assert response.status_code == 401

        valid_login_form = LoginForm(email='default@example.com', password="password")
        result = checkUserCred(valid_login_form)

        response = client.get('/profile')
        assert response.status_code == 200

def test_veges_page_get(client):
    response = client.get('/signup')
    assert response.status_code == 200
    assert b"Password" in response.data
    assert b"Name" in response.data








