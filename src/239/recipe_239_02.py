from bs4 import BeautifulSoup

html = '<html><body><div id="content"><h1>chapter 1</h1><p class="para1">paragraph1</p> <p class="para2">paragraph2</p><div></body></html>'
soup = BeautifulSoup(html, "html5lib")

content = soup.find(id="content")
print(content)
