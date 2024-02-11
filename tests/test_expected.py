from application.forms import * 
from bs4 import BeautifulSoup
from flask import url_for
import pytest 

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