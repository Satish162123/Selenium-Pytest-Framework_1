import pytest 
from api.helpers.api_client import ApiClient 
 
@pytest.mark.api 
def test_get_users(): 
    client = ApiClient() 
    response = client.get("/users") 
 
    assert response.status_code == 200 
    data = response.json() 
    assert "users" in data 
    assert len(data["users"]) > 0 
 
 
@pytest.mark.api 
def test_create_user(): 
    client = ApiClient() 
    payload = { 
        "firstName": "Satish", 
        "lastName": "QA", 
        "age": 28 
    } 
 
    response = client.post("/users/add", payload) 
 
    assert response.status_code == 201 
    body = response.json() 
    assert body["firstName"] == "Satish" 
 
 
@pytest.mark.api 
def test_update_user(): 
    client = ApiClient() 
    payload = { 
        "age": 29 
    } 
 
    response = client.put("/users/1", payload) 
    assert response.status_code == 200 
 
 
@pytest.mark.api 
def test_get_invalid_user(): 
    client = ApiClient() 
    response = client.get("/users/99999") 
 
    assert response.status_code == 404