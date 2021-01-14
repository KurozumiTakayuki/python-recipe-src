import requests

r = requests.get("https://httpbin.org/get")

# エンコーディング
print(r.encoding)

# httpステータスコード
print(r.status_code)

# レスポンスヘッダ
print(r.headers)
