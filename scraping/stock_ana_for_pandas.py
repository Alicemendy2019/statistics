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
	topix_30_list.to_csv('STOOQ/'+dt.date.today().strftime('%Y%m%d')+'_topix30.txt')
	return topix_30_list

def get_nikkei_225():
	urlOrg=r'https://stooq.com/t/?i=589&v=0&l='
	# nikkei_225 = []
	url = urlOrg + str(1)
	data = pd.read_html(url)
	nikkei_225 = data[1][5:-1]
	for i in range(2,4):
		url = urlOrg + str(i)
		data = pd.read_html(url)
		nikkei_225 = nikkei_225.append(data[1][5:-1])
		# if float(data[1]["No."][5:-1].tail(1)) == 1.0:
		#	 break
	print(nikkei_225.head())
	print(nikkei_225.tail())
	nikkei_225.to_csv('STOOQ/'+dt.date.today().strftime('%Y%m%d')+'_nikkei225.txt')
	return nikkei_225

def get_japan_code():
	urlOrg=r'https://stooq.com/t/?i=519&v=0&l='
	url = urlOrg + str(1)
	data = pd.read_html(url)
	japan_code = data[1][5:-1]
	for i in range(2,39):
		url = urlOrg + str(i)
		data = pd.read_html(url)
		japan_code = japan_code.append(data[1][5:-1])
	print(japan_code.head())
	print(japan_code.tail())
	japan_code.to_csv('STOOQ/'+dt.date.today().strftime('%Y%m%d')+'_nikkei225.txt')
	return japan_code

def get_comp_stock_data(code,start=None,end=None):

	if start is None:
		today=dt.date.today()
		last_year=str(int(today.year)-1)
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
	print(data[0].head(10))
	print(data[0].tail())
	df_stock = data[1][5:-1]

	for i in range(2,12):
		url = url_3 + str(i)
		data = pd.read_html(url)
		df_stock = df_stock.append(data[1][5:-1])
		if float(data[1]["No."][5:-1].tail(1)) == 1.0:
			break
		# print(df_stock.head())
		# print(df_stock.tail())
	return df_stock,start,end

def update_data(df_stock):

	df_stock.dropna(subset=['Volume'],axis=0,inplace=True)
	df_stock["Date2"] = [dt.datetime.strptime(i, "%d %b %Y") for i in df_stock["Date"]]
	# indexの設定
	df_stock.set_index("Date2",inplace=True)
	df_stock.drop(['No.'],axis=1,inplace=True)
	return df_stock

if __name__ == '__main__':

	start=None
	end=None
	while True:
		indata=input('数値で入力してください\n1:TOPIX30情報取得\n2:NIKKEI情報取得\n\
3:特定コード株価取得\n4:グラフ出力\n5:日本証券コード情報取得\n9:終了\n---> ')
		if indata == '1':
			topix_30=get_topix_30()
			print(topix_30.loc[:,['Symbol','Name']])
			# sys.exit()
		elif indata == '2':
			nikkei_225=get_nikkei_225()
			print(nikkei_225.loc[:,['Symbol','Name']])
		elif indata == '3':
			code=input('コードを入力してください')
			start=input('始点日を入力してください')
			end=input('終点日を入力してください')
			df_stock,start,end=get_comp_stock_data(code,start,end)
			df_stock=update_data(df_stock)
			df_stock.to_csv('STOOQ/{code}_{start}_{end}.csv'.format(code=code,start=start,end=end))
		elif indata == '4':
			# プロット 縦軸（指定）×横軸（インデックス？）
			df_stock["Close"].astype(float).plot(title='Stock Price',grid=True)
			plt.show()
		elif indata == '5':
			japancode=get_japan_code()
			# print(japancode.loc[:,['Symbol','Name']])
			print('finish')
		elif indata == '9':
			print('終了します')
			sys.exit()
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
