# class 類別名稱:
#     def__init__(self):         #定義初始化函式
# 建立實體物件 放入變數obj中
# obj=類別名稱() #呼叫初始化函式

# class Point:
#     def __init__(self):
#         self.x=3
#         self.y=4
# # 建立實體物件
# # 此時體物件包含x和y兩個實體屬性
# p=Point()


#point實體物件的設計;平面座標上的點
# class point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
# p1=point(3,4)
# print(p1.x,p1.y) #建立第一個實體物件

# p2=point(5,6)
# print(p2.x,p2.y) #建立第二實體物件


#fullname
class fullname:
    def __init__(self,flist,last):
        self.flist=flist
        self.last=last
name1=fullname("G.Y.","M.Y.")
print(name1.flist,name1.last)
name2=fullname("A.B.","C.D.")
print(name2.flist,name2.last)
