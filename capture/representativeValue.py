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

def interquartile_range(datas):
  datas.sort() #昇順に並べ替え
  datas_len = len(datas) #データ数
  dev_number = datas_len / 2 #データ数の半分(データの中央)
  median_value = median(datas) #median関数を呼び出し、中央値を格納
  if datas_len % 2 == 0: #データ数を２で割ったときの余りが０の場合（※つまり偶数）
    lower_datas = datas[:int(dev_number)] #[開始番号:終了番号-1]の構文 真ん中より下のリスト
    higher_datas = datas[int(dev_number):] # 真ん中より上のリスト
  else:
    lower_datas = datas[:int(math.floor(dev_number))]
    higher_datas = datas[int(dev_number)+1:]
  firstQuartile = median(lower_datas)
  thirdQuartile = median(higher_datas)
  return '第1四分位点: ' + str(firstQuartile) + ' 第2四分位点: ' + str(median_value) + ' 第3四分位点: ' + str(thirdQuartile)

def geometrical_mean(datas):
  datas.sort() #昇順に並べ替え
  datas_len = len(datas) #データ数  
  Infinite_product = 1
  for data in datas:
    Infinite_product = data * Infinite_product
  geometrical_mean_value = pow(Infinite_product,1/datas_len ) #n乗するデフォルト関数 ｎ乗根＝1/n乗
  return '総乗値：' + str(Infinite_product) + ' ' + '相乗平均値：' + str(geometrical_mean_value)

def harmonic_mean(datas): #それぞれの区間距離は１ｋｍとする
  datas_len = len(datas) #データ数かつ距離（ｋｍ）
  total_time = 0
  for data in datas:
    total_time = total_time + (1 / data)
  harmonic_mean_value = datas_len / total_time
  return '総時間：' + str(total_time) + ' ' + '調和平均値：' + str(harmonic_mean_value)

def variance(datas):
  datas_len = len(datas) #データ数
  average_value = average(datas) #平均値を取得する
  sumdata = 0
  for data in datas:
    data1 = data - average_value
    sumdata = sumdata + pow(data1,2) #2乗するした値の総和
  variance_value = sumdata / (datas_len-1)
  return variance_value

def standard_deviation(datas):
  variance_value = variance(datas)
  standard_deviation_value = pow(variance_value,1/2)
  return standard_deviation_value

datas1 = [26,24,21,19,19,18.5,18,18,18,15,14,13,12,12,11,8,6,6,6,2]
print(sum(datas1))
print(average(datas1))
print(median(datas1))
print(mode(datas1))
print(variance(datas1))
print(standard_deviation(datas1))


# C:\Users\amepa\Documents\仕事\beyoufree\Python\statistics\capture

# ## データ整理
# 1. 代表値
#   1. 平均値
#   1. 中央値 第1四分位点 第3四分位点 50％ 25％ 75％
#   1. 最頻値
# 2. 分散  各値-平均値の２乗の和 ÷ 変数の数-1
# ※各値-平均値の２乗の和 ÷ 変数の数 == 変数の２乗の和 - 変数の数＊平均値の２乗
# 3. 標準偏差 分散の平方根
#   チェビシェフの不等式  k>0 // (平均値-k標準偏差) <= (1-(1/k^2)) <= (平均値+k標準偏差) 観測値の広がりを抑えるのに有効らしい
# 4. 安定分布尺度  異常値に対応する
#   標準偏差の代わり → 四分位範囲 ＝ 第3四分位点 - 第1四分位点 cf.十分位範囲

#   「全国消費実体調査報告」 → 全国家計構造調査
#   /home/yohey/ドキュメント/python/statistics/全国消費実態調査平成21年全国消費実態調査全国貯蓄負債編.csv

#   |a |a |a |
#   |-|-|-|
#   |a |a |a |

# 5. 度数分布表 eX 株の前日比と度数（重複数）
#     1. 階級分け 
#         1. スタージェスの公式 1+3.3\*logN
#     1. 階級平均値（中点）
#     1. 度数
#     1. 相対度数 （度数/総度数） 相対度数分布
#     1. 累計度数 （総度数）
#     1. 累計相対度数  （合計が1）

# 6. ヒストグラム 度数分布表を棒グラフにした ※階級幅に合わせて設定する
#   度数分布多角形 ヒストグラムを折れ線にした

# 7. ローレンツ曲線  不平等度を計測する 累計相対所得等
#   ジニ係数  = 1-ローレンツ曲線下の多角形面積/三角形面積  ＝２\*{相対順位と相対所得の積の総和} - n+1/n

# 8. 切り落とし平均  安定特性値の１つ　（cf.中央値） 
#   最大値と最小値とその周辺を切り落とした平均値  スポーツ採点等
# 9. 幾何平均 （cf.平均値）  観測値の積を求め、ｎ乗根とする 利子率の平均等（MMCmoney market certificate 金利の上限と連動する預金）1年目～3年目の金利が違う場合、同じ増加率とみなす
# 10. 移動平均  時系列データで特有な変化を考慮しないよう  四半期報
#   加重移動平均  特定の機関から前後の値に重みづけして総和を１になる平均
# 11. 加重平均値 重みの総和は１になるよう
# 12. 範囲  最大値と最小値の差
# 13. 変動係数  測定単位や平均値に依存しない代表値 力士の体重の標準偏差等
#   CV = 標準偏差/平均 = {1/n\*(X1/X_-1)^2}^1/2
#   失業率１２％から８％と３％から２％は変動係数の観点からは同様
# 14. 変数の標準化と偏差値
#   標準 =（X-平均）/標準偏差
# 15. 2変数データ  世帯の２つの特性等
#   散布図を描くのが基本
#   共分散 = Σ(ｘ－ｘの平均)(y－yの平均) / n = Σxy - (n\*x平均\*y平均)
#   相関係数 = 共分散 / √(x分散\*ｙ分散) -１ ～　＋１の間になる
# 16. 2変数同時度数分布表  縦y横x