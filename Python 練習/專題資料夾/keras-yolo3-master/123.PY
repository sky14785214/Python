from io import BytesIO
import time
from PIL import Image
import pytesseract
import requests
from selenium import webdriver


class MaoYan(object):
    def __init__(self):
        self.url = 'http://maoyan.com/films/1200486'

    def run(self):
        # 建立chrome物件,傳送selenium請求,獲取全屏物件
        chrome = webdriver.Chrome('/home/python/Desktop/chromedriver')
        chrome.implicitly_wait(5)   # 設定瀏覽器隱式等待 頁面載入
        chrome.get(self.url)

        # 讓背景變白色和文字變黑色，更易識別
        chrome.execute_script('document.querySelector(".banner").style.background = "white"')
        chrome.execute_script('document.querySelector(".stonefont").style.color = "black"')

        screen_shot = chrome.get_screenshot_as_png()   # 獲取全屏截圖的物件
        screen_image = Image.open(BytesIO(screen_shot))  # 以IO的形式轉換為二進位制,建立圖片物件
        screen_image.save('15_screen_image.png')

        # 獲取評分元素物件,計算評分元素的位置區域資訊,擷取評分圖片
        el_score = chrome.find_element_by_xpath('//span[@class="index-left info-num "]/span[@class="stonefont"]')
        height = el_score.size['height']
        width = el_score.size['width']

        left = el_score.location['x']
        top = el_score.location['y']
        right = left + width
        bottom = top + height

        cut_info = (left, top, right, bottom)
        print(cut_info)

        cut_image = screen_image.crop(cut_info)
        cut_image.save('15_cut_image.png')

        # 使用tesseract庫,進行文字識別
        try:
            score = pytesseract.image_to_string('15_cut_image.png', config='-psm 7')
            print(score)
        except Exception as e:
            print(e)
            print('識別失敗')


if __name__ == '__main__':
    mao_yan = MaoYan()
    mao_yan.run()