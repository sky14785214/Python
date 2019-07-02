import os#開啟檔案時需要 
import cv2

Data_path='e:\data\image' 
list=os.listdir(Data_path)
# print(list)
for Data_0 in list:
    path=Data_path+Data_0
    # print(path)
    # im=cv2.imread(path)
    # res=cv2.resize(im,(1280,1280),interpolation=cv2.INTER_CUBIC)
    # cv2.imwrite("datatest",res)

    img=cv2.imread(path)
    res=cv2.resize(img,(1280,1280),interpolation=cv2.INTER_AREA)
    # cv2.imshow('out'+ Data_0 +'.jpg',res)
    cv2.imwrite('out'+ Data_0 +'.jpg',res)
    cv2.waitKey(0)
    # cv2.destroyAllwindows()
    