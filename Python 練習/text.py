#coding=utf-8 
import os#開啟檔案時需要 
from PIL import Image 
import re 
Start_path='F:/image/' 
iphone5_width=1136 
iphone5_depth=640 
list=os.listdir(Start_path) 
#print list 
count=0 
for pic in list: 
    path=Start_path+pic 
    print path 
    im=Image.open(path) 
    w,h=im.size 
#print w,h 
#iphone 5的解析度為1136*640,如果圖片解析度超過這個值,進行圖片的等比例壓縮 
if w>iphone5_width: 
    print pic 
    print "圖片名稱為"+pic+"圖片被修改" 
    h_new=iphone5_width*h/w 
    w_new=iphone5_width 
    count=count+1 
    out = im.resize((w_new,h_new),Image.ANTIALIAS) 
    new_pic=re.sub(pic[:-4],pic[:-4]+'_new',pic) 
    #print new_pic 
    new_path=Start_path+new_pic 
    out.save(new_path) 
if h>iphone5_depth: 
    print pic 
    print "圖片名稱為"+pic+"圖片被修改" 
    w=iphone5_depth*w/h 
    h=iphone5_depth 
    count=count+1 
    out = im.resize((w_new,h_new),Image.ANTIALIAS) 
    new_pic=re.sub(pic[:-4],pic[:-4]+'_new',pic) 
    #print new_pic 
    new_path=Start_path+new_pic 
    out.save(new_path) 
    print 'END' 
    count=str(count) 
    print "共有"+count+"張圖片尺寸被修改" 