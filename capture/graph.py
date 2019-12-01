import matplotlib.pyplot as plt
import numpy as np
import representativeValue as rv

data = np.random.randint(0, 100, 30) #0から１００までの整数値を30個生成

average_value = rv.average(data)

fig,ax = plt.subplots()
plt.plot(data) #ここを変える
ax.axhline(average_value, ls='--', color='r')

plt.show()

"""
numpy
-----２から８まで２ずつ
print(np.arange(2,8,2))
-----2列5データ1未満の実数
print(np.random.rand(2,5))
-----０から５０まで整数
np.random.randint(0, 50, 50)
-----標準正規分布
np.random.randn(50)
-----平均50、標準偏差10の正規分布
np.random.normal(50,10)
"""

# fig = plt.figure()
# fig.suptitle('suptitle')

# data1,data2,data3,data4 = np.random.rand(4,100)

# fig, ax_lst = plt.subplots(2,2)
# ax_lst[0][0].set_xlim([100,200])
# ax_lst[0][1].set_ylim((30,20))
# ax_lst[1][0].set_title('3rd')
# ax_lst[1][1].set_xlabel('xlabelyade')

# plt.figure(figsize=(9,3))
# plt.subplot(131)
# plt.bar(data1,data4)
# plt.subplot(132)
# plt.scatter(data2,data4)
# plt.subplot(133)
# plt.plot(data3,data4)

# for key, value in fig.__dict__.items():
#   print(key, ':', value)

# for x in dir(fig):
# 	print (x)



# plt.show()
# plt.legend()


#ヒストグラムのため、階級数
#スタージェスの公式
# 階級数=1+3.3*logN
