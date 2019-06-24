# from PIL import Image
# import numpy as np
# import matplotlib.pyplot as plt

# from PIL import Image
# import numpy as np
# import matplotlib.pyplot as plt
# img=np.array(Image.open('e:/text0.jpg'))  #打开图像并转化为数字矩阵
# plt.figure("dog")
# # plt.imshow(img)
# plt.axis('off')
# plt.show()

# print(img.shape)  
# print(img.dtype) 
# print(img.size) 
# print(img)



# CV_INTER_NN - 最近邻插值,  

# CV_INTER_LINEAR - 双线性插值 (缺省使用)  

# CV_INTER_AREA - 使用象素关系重采样。当图像缩小时候，该方法可以避免波纹出现。当图像放大时，类似于 CV_INTER_NN 方法..  

# CV_INTER_CUBIC - 立方插值.  
# import cv2

# image=cv2.imread('C:\Users\admin\Desktop\image')
# # cv2.imshow('image',image)
# # cv2.waitKey(0)

# res=cv2.resize(image,(1280,1280),interpolation=cv2.INTER_CUBIC)
# # cv2.imshow('image2',res)

# cv2.imwrite("C:\Users\admin\Desktop\image2",res)cv2.waitKey(0)
# cv2.destoryAllWindows()


#-------
# X=int(input("請輸入X值: "))
# Y=int(input("請輸入Y值"  ))

#------

import cv2
import os

# array_of_img=[]



def read_directory(directory_name):
    for filename in os.listdir(directory_name):
        print(filename)
        
        
read_directory('E:\GitHub\專題資料夾\Data\image')