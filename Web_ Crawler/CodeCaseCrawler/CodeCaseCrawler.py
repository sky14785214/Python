# 匯入套件
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import json
import requests



    
# 啟動瀏覽器工具的選項  #https://the.annswer.org/t/topic/585
options = webdriver.ChromeOptions()
# options.add_argument("--headless")              #不開啟實體瀏覽器背景執行
# options.add_argument("--start-maximized")         #最大化視窗
options.add_argument("--incognito")               #開啟無痕模式
options.add_argument("--disable-popup-blocking ") #禁用彈出攔截

# 使用 Chrome 的 WebDriver
driver = webdriver.Chrome(executable_path='./CodeCaseCrawler/chromedriver.exe',options = options)


# 螢幕最大化
driver.maximize_window()

# 放置 FB 個人發文的基本資訊
listPost = []

# 前往 FB
def begin():    
    # 走訪網址
    driver.get('https://www.facebook.com/')

# 登入
def login():
    # 輸入帳號
    inputEmail = driver.find_element_by_id('email') 
    inputEmail.send_keys("a14785214s@yahoo.com.tw")

    # 輸入密碼
    inputPwd = driver.find_element_by_id('pass')

    inputPwd.send_keys("Sky25896325@")

    # 按下登入/送出鈕
    btnSubmit = driver.find_element_by_css_selector('button[type="submit"][name="login"]')
    btnSubmit.click()
    
    # 強制等待
    sleep(3)

# 走訪個人頁
def visit():
    driver.get('https://www.facebook.com/groups/2276905072551692')

# 捲動頁面
def scroll():
    # 瀏覽器內部的高度
    innerHeightOfWindow = 0
    
    # 當前捲動的量(高度)
    totalOffset = 0

    # 每捲一次，休息幾秒
    sleepingSecond = 1
    
    # 在捲動到沒有元素動態產生前，持續捲動
    while totalOffset <= innerHeightOfWindow:
        # 每次移動高度
        totalOffset += 300;
        
        # 捲動的 js code
        js_scroll = "(function (){{window.scrollTo({{top:{}, behavior: 'smooth' }});}})();".format(totalOffset)
        
        # 執行 js code
        driver.execute_script(js_scroll)
        
        # 強制等待
        sleep(sleepingSecond)
        
        # 透過執行 js 語法來取得捲動後的高度
        innerHeightOfWindow = driver.execute_script('return window.document.documentElement.scrollHeight;');
        
        # 強制等待
        sleep(sleepingSecond)
        
        # 印出捲動距離
        # print("innerHeightOfWindow: {}, totalOffset: {}".format(innerHeightOfWindow, totalOffset))
        
        # 為了實驗功能，捲動超過一定的距離，就結束程式
        if totalOffset > 3000:
            break

# 分析元素內容
def parse():
    # 確認當前動個人態牆的發文數量
    cssSelectorPost = 'div[data-ad-comet-preview="message"] span[dir="auto"]'
    temp = []

    try:
        # 取得元素
        div = driver.find_elements_by_css_selector(cssSelectorPost)

        # 將每個發文的內容擷取出來
        for index, elm in enumerate(div):
            
            # print("index: {}".format(index))
            # print("text: {}".format(elm.text))
           
            # print()
            
            # 將資料新增到 list 當中
            # listPost.append({
            #     "index": index,
            #     "text":elm.text
            # })
            temp.append({
                "index": index,
                "text":elm.text
            })
        # 將放置發文的 list，以 JSON 格式存入檔案
        # fp = open("FB.json", "w",encoding='UTF-8')
        # fp.write( json.dumps(listPost, ensure_ascii=False) )
        # fp.close()
    
    

    except TimeoutException:
        print('等待逾時！')
    
    return temp #最新列表

# 關閉瀏覽器
def end():
    # 關閉瀏覽器
    driver.quit()


def send_fittt(message): # 發送 v1 訊息至line訊息
    url = (
        "https://maker.ifttt.com/trigger/sky14785214/with/"+
        "key/bT2vBqUupdmzQ6YZakbjOI"+
        "?value1=" + str(message)

        )
    # 發送line通知
    r = requests.get(url)
    if r.text[:15] == "Congratulations":
        print(" 已傳送: "+ str(message) +"到Line")

    return r.text

def OpenJson(JsonFile):        
    with open(JsonFile,encoding="utf-8") as f:
        data = json.load(f)
    return data

def GetJson_1to3(StartNumber,EndNumber,Spase,Json1to3): # 讀取json列表篩選
    OldPost = []    
    for i in range(StartNumber,EndNumber,Spase):
        # print(FBdata[i]['text'])
        # print("-----------------------------------")
        OldPost.append(Json1to3[i]['text'])
    return OldPost

def DifferenceListValue(List1,List2): #讀取兩個列表 反傳兩列表不同的值
    DiffValue= []
    for x in List1:
        if x in List2:
            pass
        else:
            DiffValue.append(x)
    return DiffValue





# 主程式
if __name__ == '__main__':
    # OpenGoogleDriver()
    begin()
    login()
    while True:
        visit()
        scroll()

        sleep(30)
        
        NewPosytemp = parse() #解析網頁資料
        NewPosy= GetJson_1to3(1,4,1,NewPosytemp) # 取出最新3篇文章
        # print(NewPosy)

        #----- 取出舊資料
        OldPost = []    
        # FBJsonPath= "F:\GitHub\CodeCaseCrawler\FB.json"
        FBdata= OpenJson("F:\GitHub\CodeCaseCrawler\FB.json")  
        OldPost = GetJson_1to3(1,4,1,FBdata)
        #------

        #-----發送訊息
        sendmessage = DifferenceListValue(NewPosy,OldPost)
        if len(sendmessage) != 0:
            send_fittt(str(sendmessage))
        #--------
        print(NewPosy)

        # 處存貼文 做舊資料
        fp = open("F:\GitHub\CodeCaseCrawler\FB.json", "w",encoding='UTF-8')
        fp.write( json.dumps(NewPosytemp, ensure_ascii=False) )
        fp.close()



    end()
