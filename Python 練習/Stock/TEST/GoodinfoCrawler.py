
from sqlite3 import DatabaseError
import urllib.request as req
import bs4

def GoodinfoData(GoodinfoDividendUrl): #查詢股票在Goodinfo 股利政策的html
    

    GoodinfoDividendUrl = "https://goodinfo.tw/tw/StockDividendPolicy.asp?STOCK_ID=" + GoodinfoDividendUrl 

    # url="https://histock.tw/stock/financial.aspx?no=2887&t=2"

    #附加headers 偽裝一般使用者
    request = req.Request(GoodinfoDividendUrl, headers={
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
    })

    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
        # print(data)
    temp = bs4.BeautifulSoup(data,"html.parser")

    return temp
def GoodinfoDataDividend(bs4Data):
    time = bs4Data.find_all("b")
    # for i in range(11,15,1):
        

    print(time)

    # time = time[11]
    # time = time.string
    # temp = bs4Data.find_all("td" ,title="0.605") # 尋找最新年度現金股利

    # return temp



IntPutStockNumber=repr(input("請輸入查詢股票代號:"))
Goodinfobs4= GoodinfoData(IntPutStockNumber) #取得IntPutStockNumber在GOODinfo的股利政策網頁資料
Dividend = GoodinfoDataDividend(Goodinfobs4)

print(Dividend)