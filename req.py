import requests
res = requests.post('http://localhost:5000/login', json={"username": "varoo","password":"varoo"})
if res.ok:
    print("Worked")
