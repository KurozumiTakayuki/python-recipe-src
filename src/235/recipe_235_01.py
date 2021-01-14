import requests

url = "https://httpbin.org/get"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.63 Safari/537.36'}
r = requests.get(url, headers=headers)
print(r.text)
