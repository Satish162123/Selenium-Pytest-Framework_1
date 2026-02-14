import pytest
from jsonschema import validate
from api.helpers.api_client import APIClient
from api.schemas.users_schema import users_schema


@pytest.mark.api
def test_get_users_schema():
    client = APIClient()
    response = client.get("/users")

    assert response.status_code == 200
    validate(instance=response.json(), schema=users_schema)


@pytest.mark.api
def test_create_user():
    client = APIClient()

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
def test_invalid_user():
    client = APIClient()
    response = client.get("/users/99999")

    assert response.status_code == 404


@pytest.mark.api
def test_response_time():
    client = APIClient()
    response = client.get("/users")

    assert response.elapsed.total_seconds() < 2
