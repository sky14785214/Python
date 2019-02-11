#檔案物件=open(檔案路徑,mode=開啟模式)
# 讀取模式 - r
# 寫入模式 - w
# 讀寫模式 - r+

# 讀寫檔案
# 檔案物件.read()
# for 變數 in 檔案物件
#     從檔案依序讀取每行文字到變數

# 讀取JSON格式
# import 讀取json格式
# 讀取到的資料=json.load(檔案物件)

#寫入文字
#檔案物件.write(字串) \n可以換行

#寫入json格式
# import json
# json.dump(要寫入的資料,檔案物件)

#檔案物件.close() 關閉檔案

#---
#最佳實務寫法 可以不必寫入關閉 執行結束自動關閉
# with open(檔案路徑,mode=開啟模式)as 檔案物件:
#     讀取或寫入檔案程式
#以上區塊會自動 安全的關閉檔案
#----

#儲存檔案
# file=open("data.txt",mode="w",encoding="utf-8") #開啟 #encoding=編碼 utf-8 是中文編碼
# file.write("Help python\nsencond line\n測試中文") #操作
# file.close() #關閉
#--
#最佳實務寫法
# with open("data.txt",mode="w",encoding="utf-8") as file:
#     file.write("Help python\nsencond line\n測試中文\n測試務實")
# #---

# #讀取檔案
# with open("data.txt",mode="r",encoding="utf-8") as file:
#     data=file.read()
# print(data)

#把檔案中資料一行一行讀取並總和
# with open("data.txt",mode="w",encoding="utf-8") as file:
#     file.write("3\n5\n")
# sum=0
# with open("data.txt",mode="r",encoding="utf-8") as file:
#     for line in file: #一行一行的讀取
#         sum+=int(line)
# print(sum)

#-----json
# import json
# with open("config.json",mode="r") as file:
#     data=json.load(file)
# print("name: ",data["name"])
# print("version: ",data["version"])

#檔案中讀取json資料,放變數data裡面
import json
with open("config.json",mode="r") as file:
    data=json.load(file)
print(data) #data是字典資料
data["name"]="new name" #修改變數資料
#把最新的資料複寫回檔案中
with open("config.json",mode="w") as file:
    json.dump(data,file)
