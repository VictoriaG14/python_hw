import requests
from config import url
from config import token

def test_update_project():
    headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
    }

    data = {
        "deleted": 'true',
        "title": "testProjectPython20"
    }
    response = requests.put(url + '/4a0daa00-ff21-41d6-b723-023fe48e240a', headers=headers, json=data)
    assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"