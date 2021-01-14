# 技術評論社の新刊情報のURLやhtmlの構造が変化した場合、このコードは正しく実行できません。
# その場合は変数htmlのデータ内容を同梱しているgihyo.htmlに置き換えてください。
# 以下は置き換え例となります。
# with open("gihyo.html", "r") as f:
#     html = f.read()

import requests
from bs4 import BeautifulSoup

# 新刊のURL
url = "https://gihyo.jp/book/list"

# HTTP GETリクエスト
r = requests.get(url)

# htmlの取得
html = r.text

# htmlのパース
soup = BeautifulSoup(html, "html5lib")

# ulタグの取得
ul = soup.find("ul", class_="magazineList01 bookList01")

# ulタグ配下のliタグをシーケンスで取得
lis = ul.find_all("li")

# liタグ毎に書籍情報を取得
for li in lis:
    link = li.find("h3").find("a")
    print(link.text, link.get("href"))
