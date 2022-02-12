import twstock
#----
# stock2887.fetch(2018,7) #設定你獲取年月 否則預設近31日
# stock.fetch(2010, 5)  # 獲取 2010 年 5 月之股票資料
# stock.fetch_31()      # 獲取近 31 日開盤之股票資料
# stock.fetch_from(2000, 10)  # 獲取 2000 年 10 月至今日之股票資料
#-----
stock2887 = twstock.Stock("2887")
# stock2887.sid #回傳股票代號
# stock2887.price #回傳各日(31天)收盤價
# stock2887.high # 各日之最高價
# stock2887.data #回傳資料之對應日期
# stock2887.moving_average(stock2887.price, 5)
# stock2887.moving_average(stock2887.capacity, 5)  # 計算五日平均交易量 ---
# stock2887.ma_bias_ratio(5, 10)  # 計算五日、十日乖離值


# print(stock2887.sid)
# print(len(stock2887.price)) #len 列表長度
# print(stock2887.price)
# print(stock2887.high)
# print(stock2887.data)
# print(stock2887.fetch)
# print(stock2887.moving_average(stock2887.price, 20))
# print(stock2887.moving_average(stock2887.capacity, 5)  ---
print(stock2887.ma_bias_ratio(5, 20))