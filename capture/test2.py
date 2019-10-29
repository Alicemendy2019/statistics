import csv
# import representativeValue as rv #representativeValue.pyをrnという名前で読み込む .pyは不要
import test as rv

filename = 'sampledata.csv'
with open(filename) as f:
	r = csv.reader(f, delimiter=',')
	rows = [[int(ll) for ll in l] for l in r]
	row = rows[0]
	print('取り込んだデータ：'+str(row))
	row.sort()
	print('ソート後のデータ：'+str(row))
	print('平均値：'+str(rv.average(row)))
	print('中央値：'+str(rv.median(row)))
	print('最頻値：'+str(rv.mode(row)))
	

# import random
# filename = 'sampledata.csv'
# text = ''
# for i in range(0,10):
# 	text += str(random.randint(1,10))

# with open(filename,'w')  as f:
# 	f.write(','.join(text))

