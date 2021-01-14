from bs4 import BeautifulSoup

html = "<html><body><h1>chapter 1</h1><p>paragraph1</p> <p>paragraph2</p></body></html>"
soup = BeautifulSoup(html, "html5lib")
h1 = soup.find("h1")
print(h1.text)
