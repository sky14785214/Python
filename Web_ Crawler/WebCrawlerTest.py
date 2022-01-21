from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
 
 # -- 取消網頁彈出視窗
options = Options() 
options.add_argument("--disable-notifications")
 # -- 

chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
chrome.get("https://www.facebook.com/groups/2276905072551692")

email = chrome.find_element_by_id("email") # 尋找html id為email欄位
password = chrome.find_element_by_id("pass")

email.send_keys('a14785214s@yahoo.com.tw') # 模擬輸入
time.sleep(1)
password.send_keys('Sky25896325@')
password.submit() 

chrome.get("https://www.facebook.com/groups/2276905072551692")