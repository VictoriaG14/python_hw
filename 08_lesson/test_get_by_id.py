import requests

url = "https://ru.yougile.com/api-v2/projects/384b585d-82bb-4180-a0d8-944a15066993"
token = "token"
def test_get_by_id():
    headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
    }

    data = {
        "deleted": 'false',
        "title": "testProjectPython"
    }
    response = requests.put(url, headers=headers, json=data)