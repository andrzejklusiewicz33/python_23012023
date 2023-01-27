import requests
response=requests.get("http://localhost/fruit.json")
print(response.json())
print(response.json()['name'])