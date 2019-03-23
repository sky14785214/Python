import twstock
#----
# stockdata.fetch(2018,7) #設定你獲取年月 否則預設近31日
# stock.fetch(2010, 5)  # 獲取 2010 年 5 月之股票資料
# stock.fetch_31()      # 獲取近 31 日開盤之股票資料
# stock.fetch_from(2000, 10)  # 獲取 2000 年 10 月至今日之股票資料
#-----
# stockdata = twstock.Stock("data")
# stockdata.sid #回傳股票代號
# stockdata.price #回傳各日(31天)收盤價
# stockdata.high # 各日之最高價
# stockdata.data #回傳資料之對應日期
# stockdata.moving_average(stockdata.price, 5)
# stockdata.moving_average(stockdata.capacity, 5)  # 計算五日平均交易量 ---
# stockdata.ma_bias_ratio(5, 10)  # 計算五日、十日乖離值


# print(stockdata.sid)
# print(len(stockdata.price)) #len 列表長度
# print(stockdata.price)
# print(stockdata.high)
# print(stockdata.data)
# print(stockdata.fetch)
# print(stockdata.moving_average(stockdata.price, 20))
# print(stockdata.moving_average(stockdata.capacity, 5)  ---
# print(stockdata.ma_bias_ratio(5, 20))

data=str(input("請輸入你想查詢的股票代號: "))
# print("你想知道的資訊: ")
Stockdata=twstock.Stock(""+str(data))
# Stockdata=twstock.Stock("2887")
StockNews=input("你想知道的資訊:\n1.回傳各日(31天)收盤價\n2.各日之最高價\n3.計算N日平均交易量\n4.計算乖離值\n5.計算KD值\n" )
if StockNews=="1":
    print(Stockdata.price)
elif StockNews=="2":
    print(Stockdata.high)
    # print(Stockdata.high[30:31])

    # one=Stockdata.price
    # one1=min(one)
    # print(one1)

elif StockNews=="3":
    averagedata=str(input("請輸入幾天內的平均交易量:"))
    print(Stockdata.moving_average(Stockdata.capacity,averagedata))
    # print(Stockdata.moving_average(Stockdata.capacity,5))
elif StockNews=="4":
    print(Stockdata.ma_bias_ratio(5,20))

elif StockNews=="5":
    print("\n穩定成長公司、ETF\n不適合長時間盤整\n當KD<20可買進，KD>80及賣出")
    TodayPrice=Stockdata.price[30:31]               #今日收盤
    TodayPrice0=TodayPrice[0]
    # print(TodayPrice0)

    NineDayLowList=Stockdata.price[23:31]           #近9天內最低價
    NineDayLowMin=min(NineDayLowList)
    # print(NineDayLowMin)

    NineDayLowList2=Stockdata.price[23:31]          #近9天最高價
    NineDayLowMax=max(NineDayLowList2)
    # print(NineDayLowMax)
    
    KD=((TodayPrice0)-(NineDayLowMin))/((NineDayLowMax)-(NineDayLowMin))*100
    print(data,"KD值為:",KD)
# elif StockNews=="6":


else:
    print("無效輸入")