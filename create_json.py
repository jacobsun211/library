import json

json_str = '{"name": "Francis", "age": 25, "city": "New York"}'

with open ('books.json','w') as f:
    data = json.loads(json_str)



print(data)