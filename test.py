import requests

BASE = "http://127.0.0.1:5000/"

headers = {"Content-Type": "application/json"}
response = requests.put(BASE + "video/4", json={"name": "Sample Video", "views": 100, "likes": 10}, headers=headers)
print(response.json())
input()

response = requests.get(BASE + "video/4")
print(response.json())
input()
response = requests.delete(BASE + "video/4")
print(response.json())
response = requests.get(BASE + "video/4")
print(response.json())

