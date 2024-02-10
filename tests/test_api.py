import pytest 

@pytest.mark.parametrize("route", ['/', '/index', '/home'])
def test_index_page(client, route):
    response = client.get(route)
    assert response.status_code == 200

def test_predict_page_get(client):
    response = client.get('/predict')
    assert response.status_code == 200

def test_error_handler(client):
    response = client.get('/lmao')
    assert response.status_code == 404