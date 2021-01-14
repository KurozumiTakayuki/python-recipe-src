import requests
import json

payload = {'key1': 'value1', 'key2': 'value2'}
url = "http://httpbin.org/post"
r = requests.post(url, json=json.dumps(payload))
print(r.text)
