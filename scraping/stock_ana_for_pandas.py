# ref : https://ai-inter1.com/python-stock_scraping/
# ref: stoop.com

""" toyota
https://stooq.com/q/d/?s=7203.jp&i=d&d1=20190601&d2=20200522&l=3
    s=7203.jp：銘柄コード
    d1=20190401：検索開始日付
    d2=20190920：検索終了日付
    l=3：ページ数
"""
import pandas as pd

url_1 = r'https://stooq.com/q/d/?s=7203.jp&i=d&d1=20190601&d2=20200522&l='
i=1
url = url_1 + str(i)
data = pd.read_html(url,header=0)
# print(data)
# print(data[0])
print(data[0].head(10))
print(data[0].tail())
df_stock = data[1][5:2]
# print(df_stock.head())
# 後ろ２つもNanになっとる

for i in range(2,100):
    url = url_1 + str(i)
    data = pd.read_html(url)
    df_stock = df_stock.append(data[1][5:2])
    if float(data[1]["No."].tail(1)) == 1.0:
        break

print(data[0].head())
print(data[0].tail())
