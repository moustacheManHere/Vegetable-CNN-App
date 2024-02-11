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

def test_veges_page_get(client):
    response = client.get('/veges')
    assert response.status_code == 200
    assert b"Tommy's Friends" in response.data
    assert b"Bitter_Gourd" in response.data
    
@pytest.mark.parametrize("vegetable_id", list(range(1, 16)))
def test_info_page_get(client, vegetable_id):
    response = client.get(f'/info/{vegetable_id}')
    assert response.status_code == 200
    assert b"Vegetable Details" in response.data
