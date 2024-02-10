from application.forms import * 
from bs4 import BeautifulSoup
from flask import url_for

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

def test_error_fallback(client):
    response = client.get('/nonexistent-route')
    assert response.status_code == 404
    assert b'Page not found' in response.data