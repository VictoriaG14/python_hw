import requests
from config import url
from config import token

def test_get_by_id():
    headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
    }

    data = {
        "deleted": 'false',
        "title": "testProjectPython"
    }
    response = requests.put(url + '/384b585d-82bb-4180-a0d8-944a15066993', headers=headers, json=data)