import json

f = open("Person.json","r")
data = f.read()
f_data = json.loads(data)

print(f_data['name'])
