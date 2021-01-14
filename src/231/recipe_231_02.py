import requests

payload = {'param1': "python", 'param2': "recipe"}
r = requests.get("https://httpbin.org/get", params=payload)
print(r.text)
