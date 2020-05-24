import csv
import representativeValue as rv #representativeValue.pyをrnという名前で読み込む .pyは不要
import sys
from operator import itemgetter

##########HEADER確認##########
def check_header(fileName):
	filename = fileName
	with open(filename) as f:
		r = csv.reader(f, delimiter=',')
		rows = [l for l in r]
		cnt = 0
		for row in rows[0]:
			print(str(cnt) + " : " + row)
			cnt = cnt + 1

def lineOneAMM(filename):
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

#######ALL DATA########
def show_alldata(filename):
	with open(filename) as f:
		print (f.read())

######ALL DATA per 1########
def show_colandrowcnt(filename):
	with open(filename) as f:
		r = csv.reader(f, delimiter=',')
		colcnt = 0
		rowcnt = 0
		errcolflg = False
		for row in r:
			colcnt = colcnt + 1
			if colcnt == 1:
				rowcnt = len(row)
			if rowcnt != len(row):
				errcolflg = True
		if errcolflg == True:
			print('※相違列数あり')
		print('列数:' + str(rowcnt))
		print ('行数:' + str(colcnt))

arg1 = sys.argv[1]
filename = arg1
# check_header(filename)
show_colandrowcnt(filename)


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

# arg1 = sys.argv[1]


######ALL DATA########
# arg1 = sys.argv[1]
# text = ''
# filename = arg1
# with open(filename) as f:
# 	r = csv.reader(f, delimiter=',')
# 	rows = [l for l in r]
# 	datacol = [1,3,5,7,8]
# 	# datacol = [1,3,5,7,8,9,10,11,12]
# 	for row in rows:
# 		for i in datacol:
# 			# print(row[i])
# 			# text += itemgetter(*row)(rows[int(i)])
# 			text += row[i] + " / "
# 		print(text)
# 		text = ""
	# rows = [[ll for ll in l] for l in r]
	# print(rows[0])
	# print(rows[1])
	# datarcol = [1,3,5,7,8,9,10,11,12]
	# data_col = [k for k in range(9,50,2)]
	# for i in datarow:
	# 	text += itemgetter(*data_col)(rows[i])
