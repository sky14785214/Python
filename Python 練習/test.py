import cv2 as cv
import numpy as np


src = cv.imread("./123.jpg")
# cv.imshow('123', src)
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

# gray = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
# cv.imshow('th1', gray[1])


gaussian = cv.GaussianBlur(gray, (51, 51), 0) #cv.GaussianBlur(它是輸入圖像, (高斯內核大小x, 高斯內核大小y), 0)
# cv.imshow('gaussian', gaussian)

gaussian = cv.threshold(gaussian, 127, 255, cv.THRESH_BINARY)
gaussian = gaussian[1]
# cv.imshow('threshold', gaussian)
#-----------------------------------

kernel = np.ones((7,7), np.uint8)

dilation = cv.dilate(gaussian, kernel, iterations = 6)
cv.imshow('dilation', dilation)

# 腐蝕影象
eroded = cv.erode(gaussian, kernel)
cv.imshow('eroded', eroded)

# cv.imshow('eroded4', eroded4)
# 顯示腐蝕後的影象
cv.imshow("Eroded Image", eroded);

#----------------
edges = cv.Canny(dilation, 20, 220)

# edges = cv.threshold(edges, 127, 255, cv.THRESH_BINARY)

# 尋找輪廓
contours, hierarchy = cv.findContours(
    edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# 繪製輪廓
cv.drawContours(src, contours, -1, (0, 0, 255), 3)

x, y, w, h =cv.boundingRect(contours[0])
print(x, y, h, w)

m6 = gray[y+15:y+h-15, x+15: x+w-15] #裁切所需要的範圍 
cv.imshow('m6', m6)


cv.imshow('src', src)


cv.waitKey(0)