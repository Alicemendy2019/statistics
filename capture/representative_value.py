import math


def average (datas):
  average_value = sum(datas) / len(datas)
  return average_value


def median (datas):
  datas_len = len(datas)
  dev_number = datas_len / 2
  if datas_len < 1:
    median_value = 'err'
  elif datas_len % 2 == 0:
    if dev_number == math.ceil(dev_number):
      median_value = (datas[int(dev_number)-1] + datas[int(dev_number)]) / 2  
    else:
      median_value = (datas[int(math.ceil(dev_number))] + datas[int(math.floor(dev_number))]) / 2
  else :
    median_value = datas[int(dev_number)]
  return median_value

## リストが奇数　→　真ん中あり インデックスは奇数
## リストが偶数　→　真ん中なし インデックスは奇数OR偶数
# datas1 = [1,2,3,4,5,6,7,8,9]
# datas2 = [1,2,3,4,5,6,7,8,9,10]
# print(median(datas1))
# print(median(datas2))
# dev_number = len(datas2) / 2
# print(dev_number)
# print(math.ceil(dev_number))
# print(math.floor(dev_number))
# print (datas2[int(math.floor(dev_number))])

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