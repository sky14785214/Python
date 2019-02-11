#攝取，串接公開 網路資料

import urllib.request as request        #載入網路連線模組
import json            
test="https://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=296acfa2-5d93-4706-ad58-e83cc951863c"
with request.urlopen(test) as response:     #urlopen(網址)
    data=json.load(response)        #利用json模組處理json資料格式 .decode("utf-8")取得中文
#print(data)

#取得公司名稱 列表出來
clist=data["result"]["results"]
with open("OPEN-data.txt",mode="w",encoding="utf-8") as file:
    for company in clist:
        file.write(company["公司名稱"]+"\n")

