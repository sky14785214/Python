import cv2
import matplotlib.pyplot as plt
img0=cv2.imread("DSC_0122.jpg",255)
img=cv2.imread("DSC_0122.jpg",0) #直接讀取為灰度圖像
# coding=utf-8
# 第一個參數ret的值為True或False，代表有沒有讀到圖片
# 第二個參數是frame，是當前截取一幀的圖片。
# 使用cv2.thresh() 套件將圖片解為非黑即白

ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY) #黑白兩值
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV) #黑白兩值並反轉
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC) #得圖像為多項素值
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO) 
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
titles = ["Color","Gray","BINARY(兩值化)","BINARY_INV(反二值化)","TRUNC","TOZERO","TOZERO_INV"]

images = [img0,img,thresh1,thresh2,thresh3,thresh4,thresh5]
for i in range(7):
    plt.subplot(2,4,i+1),plt.imshow(images[i],"gray")
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()