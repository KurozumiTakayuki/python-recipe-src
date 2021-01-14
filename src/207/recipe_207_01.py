import json

data_dict = {'colors': ['red', 'green', 'blue'], 'items': [123, 456, 789],
             'users': [{'name': '鈴木', 'id': 1}, {'name': '佐藤', 'id': 5}]}
json_str = json.dumps(data_dict, indent=2, ensure_ascii=False)
print(json_str)
