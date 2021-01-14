import requests

url = "https://httpbin.org/get"
requests.get(url, timeout=(3, 30))
