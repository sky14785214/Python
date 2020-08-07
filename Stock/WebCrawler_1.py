import urllib.request as req

def inputstock(url):
    url="https://histock.tw/stock/financial.aspx?no="+ url +"&t=2"



url="https://histock.tw/stock/financial.aspx?no=2887&t=2"

#附加headers 偽裝一般使用者
request = req.Request(url, headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
})

with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
# print(data)
#解析原始碼
import bs4
root = bs4.BeautifulSoup(data,"html.parser")

EPS_5Y = []


def inputstock(url):
    url="https://histock.tw/stock/financial.aspx?no="+ url +"&t=2"




def eps(url_data,eps5y):
    EPS_bf4 = []
    titles = root.find_all("td",class_="b-b") # 尋找所有 class=title 的div標

    for i in range(2,32,5):
        EPS_bf4.append(titles[i])        

    for i in EPS_bf4:
        EPS_5Y.append(i.string)

eps(data,EPS_5Y)
print(EPS_5Y) 
