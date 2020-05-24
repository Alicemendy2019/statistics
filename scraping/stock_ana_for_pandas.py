# ref : https://ai-inter1.com/python-stock_scraping/
# ref: stoop.com

""" toyota
https://stooq.com/q/d/?s=7203.jp&i=d&d1=20190601&d2=20200522&l=3
    s=7203.jp：銘柄コード
    d1=20190401：検索開始日付
    d2=20190920：検索終了日付
    l=3：ページ数

    topix : https://stooq.com/t/?i=581
"""
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import sys

def get_topix_30():
	url = r'https://stooq.com/t/?i=581'
	data = pd.read_html(url,header=0)
	topix_30_list = data[1][5:-1]
	topix_30_list.to_csv('topix30.txt')
	return topix_30_list

def get_comp_stock_data(code,start=None,end=None):

	if start is None:
		today=dt.date.today()
		last_year=str(int(today.year)-1)
		# last_month=int(n.month)+1
		month=str(today.month).rjust(2,'0')
		day=str(today.day).rjust(2,'0')
		start=last_year+month+day
		end=today.strftime('%Y%m%d')
		print(start)
		print(end)

	url_1 = r'https://stooq.com/q/d/?s='
	url_2 = '.jp&i=d&d1={start}&d2={end}&l='.format(start=start,end=end)
	url_3 = url_1 + str(code) + url_2
	i=1
	url = url_3 + str(i)
	data = pd.read_html(url,header=0)
	# print(data)
	# print(data[0])
	print(data[0].head(10))
	print(data[0].tail())
	df_stock = data[1][5:-1]
	
	for i in range(2,12):
	    url = url_3 + str(i)
	    data = pd.read_html(url)
	    df_stock = df_stock.append(data[1][5:-1])
	    if float(data[1]["No."][5:-1].tail(1)) == 1.0:
	        break

	print(df_stock.head())
	print(df_stock.tail())

	return df_stock,start,end

def update_data(df_stock):
	
	# 行削除
	# df_stock.query('Volume pd.isnull').index
	# df_stock['2019-09-27']
	# df_stock.set_index("Volume",inplace=True)
	df_stock.dropna(subset=['Volume'],axis=0,inplace=True)
	df_stock["Date2"] = [dt.datetime.strptime(i, "%d %b %Y") for i in df_stock["Date"]]
	# indexの設定
	df_stock.set_index("Date2",inplace=True)
	df_stock.drop(['No.'],axis=1,inplace=True)
	return df_stock

if __name__ == '__main__':

	start=None
	end=None
	if len(sys.argv) < 2:
		print('code,start,endを入力してください')
		sys.exit()
	elif sys.argv[1].upper() == 'TOPIX30':
		topix_30=get_topix_30()
		print(topix_30.loc[:,['Symbol','Name']])
		sys.exit()
	elif len(sys.argv) == 4:
		start=sys.argv[2]
		end=sys.argv[3]
	code=sys.argv[1]
	df_stock,start,end=get_comp_stock_data(code,start,end)
	
	df_stock=update_data(df_stock)
	df_stock.to_csv('{code}_{start}_{end}.csv'.format(code=code,start=start,end=end))
	# プロット 縦軸（指定）×横軸（インデックス？）
	df_stock["Close"].astype(float).plot(title='Stock Price',grid=True)
	plt.show()

"""
カラム名変更
pd.rename(columns, 任意の引数)
列削除
pd.dropna(削除する列, axis = 1, その他任意の引数)
df_stockdrop(['No.'],axis=1,inplace=True)
文字列を日付に
datetime. strptime(文字列、日付の書式)
次にstrptime()を元に列Dateに格納されている日付を示した文字列を日付型に変換し、元のDataFrameに対して列Date2を追加して日付型の値を格納します。
列Dateに格納されている日付が、1 Apr 2019の書式ですので、strptime()の引数には、"%d %b %Y"を指定しています。


"""