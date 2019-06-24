import os#開啟檔案時需要 
from PIL import Image 
import re 
import 
Data_path='E:\GitHub\專題資料夾\Data\image' 
list=os.listdir(Data_path)
# print(list)
for Data_0 in list:
    path=Data_path+Data_0
    print(path)
    im=image.open(path)
