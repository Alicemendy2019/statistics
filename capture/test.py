import math

def average (datas):
  average_value = sum(datas) / len(datas)
  return average_value

def median (datas):
    datas_len = len(datas) #データ数
    dev_number = datas_len / 2 #データ数の半分(データの中央)
    if datas_len % 2 == 0: #データ数を２で割ったときの余りが０の場合（※つまり偶数）
        median_value = (datas[int(dev_number)-1] + datas[int(dev_number)]) / 2 #真ん中の2データの合計の平均値
    else:
        median_value = datas[int(math.floor(dev_number))]
    return median_value

def mode(datas):
	datas.sort()
	datas_len = len(datas)
	data1 = data2 = data3 = datas[0]
	cnt1 = cnt2 = 1
	for i in range(1,datas_len-1):
		data1 = datas[i]
		if data1 == data2:
			cnt1 = cnt1 + 1
		else:
			if cnt1 > cnt2 :
				cnt2 = cnt1
				data3 = data2
			data2 = data1
			cnt1 = 1

	if cnt1 > cnt2 :
		cnt2 = cnt1
		data3 = data2
	return str(data3) + 'が' + str(cnt2) + '回'

# datas1 = [1,2,3,2,5,2,3,4,1]
# datas2 = [1,2,3,2,5,3,1,3,2,2]
# print(mode(datas1))
# print(mode(datas2))