import urllib.request as req
import bs4
# from bs4 import BeautifulSoup



def getData(url):
    #最新PTT
    #附加headers 偽裝一般使用者
    request = req.Request(url, headers={
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    # print(data)

    #解析原始碼

    root = bs4.BeautifulSoup(data,"html.parser") #排列html階層
    # print(root)
    # print(root.prettify())
    # print(root.title.string)

    Name = []
    url = []
    titles = root.find_all("div",class_="title") # 尋找所有 class=title 的div標籤
    print(titles)
    # print(titles)
    for titles in titles:
        if titles.a != None:
            # print(titles.a.string) # 商品主題
            Name.append(titles.a.string)           
            # print(titles.a["href"]) # 產品部分網址
            url.append(titles.a["href"])

    PttTemp = "https://www.ptt.cc/"
    for i in range(0,len(url),1):
        url[i] = PttTemp + url[i]
    


    return Name,url

def CartShopCommodityUrl(url):
    temp = "https://www.ptt.cc/"
    for i in range(0,len(url),1):
        url[i] = temp + url[i]
    
    return url




CartShopUrl = "https://www.ptt.cc/bbs/CarShop/index.html" # 二手汽車版
CommodityName, CommodityUrl = getData(CartShopUrl)  # 取得網頁中品項主旨,品項販賣網址
# CommodityUrl = CartShopCommodityUrl(CommodityUrl)
print(CommodityName)
print(CommodityUrl)


