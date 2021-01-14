from urllib import parse

url = "q=%E5%A4%89%E6%95%B0&check_keywords=yes&area=default"
q = parse.parse_qs(url)
print(q)
