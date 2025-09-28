import requests
from config import url
from config import token

def test_create():
    headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
    }

    data = {
        "title": "testProjectPython20",
        }

    response = requests.post(url, headers=headers, json=data)
    response_json = response.json()
    assert "id" in response_json, "Response should contain 'id' field"
    assert response_json["id"], "Response 'id' field should not be empty"