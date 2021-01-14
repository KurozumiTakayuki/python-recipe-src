from urllib import parse

url = "https://docs.python.org/ja/3/search.html?q=%E5%A4%89%E6%95%B0&check_keywords=yes&area=default"
p = parse.urlparse(url)
print(p)
print(p.scheme)
print(p.netloc)
print(p.path)
print(p.query)
