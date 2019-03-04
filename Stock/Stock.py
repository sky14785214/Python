import urllib.request as req
URL="http://www.twse.com.tw/exchangeReport/STOCK_DAY_AVG?response=html&date=20190217&stockNo=2887"

request=req.Request(URL,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"
})

with req.urlopen(request) as response:
    data2887=response.read().decode("utf-8")
# print(data2887)

import bs4
root=bs4.BeautifulSoup(data2887,"html.parser")
# print(root.title.string)#root.title(標籤).string(文字)
price2887=root.find_all("tbody")
# print(price2887.td.string)
# print(price2887)
for td in price2887:
    print(td) 