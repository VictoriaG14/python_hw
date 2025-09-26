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
