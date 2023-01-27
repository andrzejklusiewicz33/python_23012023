def test_employees_json():
    import requests
    response=requests.get("http://localhost/employees.json")
    for e in response.json():
        print(e['first_name'],e['last_name'])

#DUPA