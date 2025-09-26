import requests

url = "https://ru.yougile.com/api-v2/projects/4a0daa00-ff21-41d6-b723-023fe48e240a"
token = "token"
def test_update_project():
    headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
    }

    data = {
        "deleted": 'true',
        "title": "testProjectPython20"
    }
    response = requests.put(url, headers=headers, json=data)