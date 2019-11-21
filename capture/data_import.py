
import csv
import representativeValue as rv #representativeValue.pyをrnという名前で読み込む .pyは不要
# import sys
from operator import itemgetter

# filename = 'sampledata.csv'
# with open(filename) as f:
# 	r = csv.reader(f, delimiter=',')
# 	rows = [[int(ll) for ll in l] for l in r]
# 	row = rows[0]
# 	print('取り込んだデータ：'+str(row))
# 	row.sort()
# 	print('ソート後のデータ：'+str(row))
# 	print('平均値：'+str(rv.average(row)))
# 	print('中央値：'+str(rv.median(row)))
# 	print('最頻値：'+str(rv.mode(row)))

# text = ''
# filename = '../data/全国消費実態調査平成21年全国消費実態調査全国貯蓄負債編.csv'
# with open(filename) as f:
# 	r = csv.reader(f, delimiter=',')
# 	rows = [[ll for ll in l] for l in r]
# 	print(rows[0])
# 	print(rows[1])
# 	datarow = [1,5,10,11,13]
# 	data_col = [k for k in range(9,50,2)]
# 	for i in datarow:
# 		text += itemgetter(*data_col)(rows[i])

# filename = 'sampledata20191017.csv'
# with open(filename,'w')  as f2:
# 	f2.write(','.join(text))

	# row = rows[0]
	# print('取り込んだデータ：'+str(row))
	# row.sort()
	# print('ソート後のデータ：'+str(row))
	# print('平均値：'+str(rv.average(row)))
	# print('中央値：'+str(rv.median(row)))
	# print('最頻値：'+str(rv.mode(row)))

arg1 = sys.argv[1]

#######ALL DATA########
with open(arg1) as f:
	print (f.read())


######ALL DATA per 1########
# with open(arg1) as f:
# 	r = csv.reader(f, delimiter=',')
# 	for row in r:
		# print('列数:' + str(len(row)))
		# print (fn.average(int(row)))
		# print (row)

######ALL DATA per 1 in array########
# with open(arg1) as f:
# 	r = csv.reader(f, delimiter=',')
# 	l = [[float(row2) for row2 in row] for row in r]
	# print('行数:' + str(len(l)))
	# print('列数:' + str(len(l[0])))
	# print((l))
	# print(l[1][1] + ' ' + l[5][1] + ' ' + l[10][1] + ' ' + l[11][1] + ' ' + l[13][1])
	# for i in range(9,50,2):
	# 	print(l[1][i] + ' ' + l[5][i] + ' ' + l[10][i] + ' ' + l[11][i] + ' ' + l[13][i])
	# for ll in l:
	# 	ll.sort()
	# 	print (fn.average(ll))
	# 	print (fn.median(ll))
# 5	世帯人員（人）
# 11	年間収入（千円）
# 10	世帯主の年齢（歳）
# 13	貯蓄現在高【千円】


# 9	平均
# 11	年間収入　200万円未満
