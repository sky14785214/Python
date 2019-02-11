# class 類別名稱:
#     def __init__(self):
#         #定義實體屬性
#     定義實體方法/函式
# #建立實體物件/函式
# obj=類別名稱()


# class 類別名稱:
#     #定義的初始化函式
#     def __inif__(self):
#         封裝在實體物件中的變數
#     def 方法名稱(self,更多自訂參數)
#         方法主體,透過SELF操作實體物件
##建立實體物件,放入變數OBJ中
# obj=類別名稱()
#-------
# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def show(self):
#         print(self.x,self.y)
#     def distance(self,targetX,targetY):
#         return ((self.x-targetX)**2+(self.y-targetY)**2)**0.5
# p=Point(3,4)
# p.show()
# result=p.distance(0,0)
# print(result)
#------

class file:
    def __init__(self,name):
        self.name=name
        self.file=None #尚未開啟的檔案 初期是none
    def open(self): #定義實體方法
        self.file=open(self.name,mode="r",encoding="utf-8")
    def read(self):
        return self.file.read()
#讀取第一個檔案
f1=file("test-class2-data0.txt")
f1.open()
data0=f1.read()
print(data0)
#讀取第二個檔案
f2=file("test-class2-data1.txt")
f2.open()
data1=f2.read()
print(data1)
