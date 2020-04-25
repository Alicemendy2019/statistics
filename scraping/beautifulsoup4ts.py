from urllib import request
from bs4 import BeautifulSoup
"""
urllib.request.urlopen関数でWebからHTMLファイルを取得して、
それをBeautiful Soup 4に渡すと、
そのHTMLファイルをツリー構造で表現したオブジェクトが得られるので、
そのオブジェクトに対して検索するなどして、
必要な情報を抽出していく
"""
url = r'https://www.atmarkit.co.jp/ait/articles/1910/18/news015.html'
# url = r'https://news.yahoo.co.jp/topics/top-picks'
res = request.urlopen(url)
soup = BeautifulSoup(res)
res.close()
print(soup)
print(dir(soup))
