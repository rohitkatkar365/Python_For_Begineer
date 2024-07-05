import json

d = my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

res = json.dumps(d)
print(res)