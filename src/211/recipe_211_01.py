from urllib import parse

text = "みかん"
url_encoded = parse.quote(text)
print(url_encoded)
