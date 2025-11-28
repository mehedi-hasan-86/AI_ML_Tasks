import json

x = '{"Name" : "MEHEDI", "age" : 21,"City" : "New York"}'

y = json.loads(x)
print(y["age"])



import json


x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

y = json.dumps(x)
print(y)