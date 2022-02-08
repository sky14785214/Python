import urllib.request as req
url="https://www.ptt.cc/bbs/movie/index.html"

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
# print(root.title.string)
titles = root.find_all("div",class_="title") # 尋找所有 class=title 的div標籤
print(titles)
for titles in titles:
    if titles.a != None:
        print(titles.a.string)
