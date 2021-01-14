from bs4 import BeautifulSoup

html = '<html><body><div id="content"><a class="inf-link" href="/support/inquiry-form">お問い合わせはこちらから</a><div></body></html>'
soup = BeautifulSoup(html, "html5lib")

a = soup.find("a")
print(a.text)
print(a.get("href"))
