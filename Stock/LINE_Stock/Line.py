
import twstock

def StockFile(path):
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


import requests
def send_fittt(v1):
    url = (
        "https://maker.ifttt.com/trigger/sky14785214/with/"+
        "key/bT2vBqUupdmzQ6YZakbjOI"+
        "?value1=" + str(v1)
        # "&valaue2 =" + str(v2) +
        # "&valaue3 =" + str(v3) 
        )
    
    r = requests.get(url)
    if r.text[:15] == "Congratulations":
        print(" 已傳送: "+ str(v1) +"到Line")

    return r.text

   

ret = send_fittt("台積電")





