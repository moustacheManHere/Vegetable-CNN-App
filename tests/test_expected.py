from application.forms import * 
from bs4 import BeautifulSoup
from flask import url_for
import pytest 
from application.models import *

@pytest.mark.xfail
def test_wrong_input_format(client,app, test_image):
    with app.test_request_context():
        response = client.post(
            url_for('predict'),
            data={'photo': (test_image, 'test.csv')},
            content_type='multipart/form-data'
        )
    assert response.status_code == 200

    soup = BeautifulSoup(response.data, 'html.parser')
    result_message = soup.find('h3', class_='mt-3').get_text(strip=True)
    assert "I'm" in result_message

@pytest.mark.xfail
def test_missing_input(client,app, test_image):
    with app.test_request_context():
        response = client.post(
            url_for('predict'),
            data={'photo': ("lol", 'test.png')},
            content_type='multipart/form-data'
        )
    assert response.status_code == 200

    soup = BeautifulSoup(response.data, 'html.parser')
    result_message = soup.find('h3', class_='mt-3').get_text(strip=True)
    assert "I'm" in result_message

@pytest.mark.xfail
@pytest.mark.parametrize("vegetable_id", [0,16]) # test boundary cases
def test_info_page_wrong(client, vegetable_id):
    response = client.get(f'/info/{vegetable_id}')
    assert response.status_code == 200
    assert b"Vegetable Details" in response.data

@pytest.mark.parametrize("invalid_params, error_message", [
    ({'name': 'Test User', 'email': 'test@example.com'}, "Missing password"),
    ({'name': 'Test User', 'password': 'password'}, "Missing email"),
    ({'email': 'test@example.com', 'password': 'password'}, "Missing name"),
    ({}, "Missing name, email, and password")
])
@pytest.mark.xfail
def test_user_init_invalid_params(invalid_params, error_message):
    test_user = User(**invalid_params)
    assert test_user is not None


INVALID_METHODS = ["PUT", "DELETE", "PATCH"]
INVALID_PATHS = ["/", "/veges", "/predict", "/login", "/signup", "/profile"]

@pytest.mark.parametrize("method, path", [
    (method, path) for method in INVALID_METHODS for path in INVALID_PATHS
])
@pytest.mark.xfail
def test_invalid_methods(client, method, path):
    response = client.open(path, method=method)
    assert response.status_code != 405

@pytest.mark.xfail
def test_history_add_remove_incomplete(app, db):
    with app.test_request_context("/history"):
        invalid_entry = History(id=1)
        db.session.add(invalid_entry)
        db.session.commit()
        assert history_entry.histID is not None 