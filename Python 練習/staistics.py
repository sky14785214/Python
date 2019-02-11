#random statistics
#載入模組
#import random

#random.choice([0,1,5,8]) 列表中隨機取一數
#random.sample([0,1,5,8],3) 列表中隨機取3數 只能<列表長度

# data=[0,1,5,8]
# random.shuffle(data) #將列表的資料 就地 隨機調換順序
# print(data)
#隨機亂數
#import random
# random.random() 隨機取0.0 ~ 1.0 之間亂數
# random.uniform(0.0,1.0)  隨機取0.0 ~ 1.0之間的亂數
#常態分配亂數
#random.normalvariate(100,10) 取得平均數,標準差10的常態分配亂數

#統計模組
# import statistics
# statistics.mean([1,4,6,9]) 計算列表中數字的平均數
# statistics.median([1,4,6,9]) 計算列表中數字的中位數
# statistics.stdev([1,4,6,9]) 計算列表中數子的標準差

#隨機模組
# import random
# data=random.choice([1,5,6,10,20]) #隨機選取列表數字
# data1=random.sample([1,5,6,10,20],3) #隨機選取3筆
# print(data)
# print(data1)
#隨機調換順序
# import random
# data=[1,5,8,20]
# random.shuffle(data)
# print(data)

#取得亂數
# import random
# data=random.random()   #0.0 ~ 1.0 亂數
# data1=random.uniform(60,100) #60 ~ 100 亂數
# print(data)
# print(data1)

#取得常態分佈亂數
#平均數100 標準差10 得到資料多數在90~110之間
# import random
# data=random.normalvariate(100,10)
# print(data)

