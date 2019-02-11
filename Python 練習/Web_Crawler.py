import urllib.request as req
URL="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=2887&MAP_YEAR=DISPATCH_YEAR&SHOW_ROTC="
#模擬一般使用者
#建立Request 物件,附加 Request Headers資訊
request=req.Request(URL,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
})

with req.urlopen(request) as response:
    TSIB=response.read().decode("utf-8")
#print(TSIB)

import bs4
root=bs4.BeautifulSoup(TSIB,"html.parser")
print(root.title.string)#root.title(標籤).string(文字)