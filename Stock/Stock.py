import urllib.request as req
StockData=repr(input("請輸入查詢股票代號:"))

URL="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID="+repr(StockData)+"&MAP_YEAR=DISPATCH_YEAR&SHOW_ROTC="

request=req.Request(URL,headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
})

with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
# print(data)

import bs4
root=bs4.BeautifulSoup(data,"html.parser")
# print(root.title.string)#root.title(標籤).string(文字)
priceData=root.find_all("table")
# print(priceData.td.string)
print(priceData)
