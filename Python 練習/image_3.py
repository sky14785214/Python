import cv2
import os
import image_2


read_directory('E:\GitHub\專題資料夾\Data\image')

for imagedata in  





image=cv2.imread(read_directory)
# cv2.imshow('image',image)
# cv2.waitKey(0)

res=cv2.resize(image,(1280,1280),interpolation=cv2.INTER_CUBIC)
# cv2.imshow('image2',res)

cv2.imwrite("E:\GitHub\專題資料夾\Data\image_2",res)cv2.waitKey(0)
cv2.destoryAllWindows()