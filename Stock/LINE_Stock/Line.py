
import twstock
import requests


def StockFile(path):  #讀取 path.txt 的內容 
    Stock_Name = []
    
    try:
        with open(path) as StockFile:
            data = StockFile.readlines()
            # sReadData = data
            # print("讀取: ",data)
            for i in data:
                s = i.split(",")
                Stock_Name.append([s[0].strip(), float(s[1]), float(s[2])])
    except:
        print("stock.txt 讀取錯誤")
    return Stock_Name

# path = "C:/Users/Yang/Desktop/GitHub/Stock/LINE_Stock/stock.txt"
# a = StockFile(path)
# print("取出: ", a)

def send_fittt(v1): #讀取
    url = (
        "https://maker.ifttt.com/trigger/sky14785214/with/"
        "key/bT2vBqUupdmzQ6YZakbjOI"+
        "?value1=" + str(v1)

        )
    # 發送line通知
    r = requests.get(url)
    if r.text[:15] == "Congratulations":
        print(" 已傳送: "+ str(v1) +"到Line")

    return r.text

def WebYahooNewStockPrice(URL): #取得網址中yahoo即時股價
    ret = send_fittt("台積電")
a = twstock.realtime.get('2330')
print(a)
# b = twstock.realtime.get([])



