import requests

payload = {'key1': 'value1', 'key2': 'value2'}
url = "https://httpbin.org/post"
r = requests.post(url, data=payload)
print(r.text)
