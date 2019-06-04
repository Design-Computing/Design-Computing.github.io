import requests
import json

url = "https://56wbk1pp93.execute-api.us-west-2.amazonaws.com/test/anotherTry"

data = {"dkey": "dval"}
r = requests.get(url, json=data)
print(r, r.json())
