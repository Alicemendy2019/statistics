
import csv
import sys
import random
import representative_value as fn

arg1 = sys.argv[1]

#######ALL DATA########
# with open(arg1) as f:
# 	print (f.read())
	

######ALL DATA per 1########
# with open(arg1) as f:
# 	r = csv.reader(f, delimiter=',')
# 	for row in r:
		# print('列数:' + str(len(row)))
		# print (fn.average(int(row))) 
		# print (row) 

######ALL DATA per 1 in array########
with open(arg1) as f:
	r = csv.reader(f, delimiter=',')
	l = [[float(row2) for row2 in row] for row in r]
	# print('行数:' + str(len(l)))
	# print('列数:' + str(len(l[0])))
	print((l))
	# print(l[1][1] + ' ' + l[5][1] + ' ' + l[10][1] + ' ' + l[11][1] + ' ' + l[13][1])
	# for i in range(9,50,2):
	# 	print(l[1][i] + ' ' + l[5][i] + ' ' + l[10][i] + ' ' + l[11][i] + ' ' + l[13][i])
	for ll in l:
		ll.sort()
		print (fn.average(ll)) 
		print (fn.median(ll)) 
# 5	世帯人員（人）
# 11	年間収入（千円）
# 10	世帯主の年齢（歳）
# 13	貯蓄現在高【千円】


# 9	平均
# 11	年間収入　200万円未満

# with open('../data/sampledata2.csv','w')  as f:
# 	for i in range(0,30):
# 		text = random.randrange(1,100)
# 		# f.write(',',str(text))
# 		f.write(','.join(str(text)))