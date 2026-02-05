import requests 
import pytest
BASE_URL = "https://dummyjson.com" 

@pytest.mark.api
def test_get_users(): 
    response = requests.get(f"{BASE_URL}/users") 
 
    # Status code validation 
    assert response.status_code == 200 
 
    # Response body validation 
    json_data = response.json() 
    assert "users" in json_data 
    assert len(json_data["users"]) > 0

@pytest.mark.api
def test_create_user(): 
    payload = { 
        "firstName": "Satish", 
        "lastName": "QA", 
        "age": 28 
    } 
 
    response = requests.post( 
        f"{BASE_URL}/users/add", 
        json=payload 
    ) 
 
    assert response.status_code == 201 
 
    json_data = response.json() 
    assert json_data["firstName"] == "Satish" 
    assert json_data["age"] == 28

@pytest.mark.api
def test_update_user(): 
    payload = { 
        "firstName": "Updated", 
        "age": 29 
    } 
 
    response = requests.put( 
        f"{BASE_URL}/users/1", 
        json=payload 
    ) 
 
    assert response.status_code == 200 
 
    json_data = response.json() 
    assert json_data["age"] == 29

@pytest.mark.api
def test_get_invalid_user(): 
    response = requests.get(f"{BASE_URL}/users/99999") 
 
    assert response.status_code == 404