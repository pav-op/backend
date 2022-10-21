import requests


json = {}
data = {
      "Id": 78912,
      "Customer": "Jason Sweet",
      "Quantity": 1,
      "Price": 18.00
}

for i in range(10):
    json[i] = {
            "Id": i,
            "data": data
     }

requests.post("http://localhost:3000", json=json)
