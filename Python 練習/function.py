#函數基礎
#定義>呼叫 先定義在呼叫
#基本語法 def函數名稱(參數名稱):
#           函數內部程式碼
#------
#先定義印出Hello的函數
#def sayHello():
#    print("Hello")
#然後呼叫上方定義的函數
#sayHello()
#------
#定義一個可以做加法的函式
#def add(n1,n2):
#    result=n1+n2
#    print(result)
#呼叫上方定義的函式
# add(3,4)
# add(7,8)
# ------
#定義函數 ，若沒有呼叫就不會執行
# def test(n1,n2):
#     print(n1*n2)
# #呼叫函數
# test(3,4)
# test(5,6)

# def test(n1,n2):
#     print(n1*n2)
#     # return n1*n2 回結束回傳 n1*n2 可不加不加 回傳值為none
# #呼叫函數
# value=test(3,4)
# print(value)
#----

# def test(n1,n2):
#     return n1*n2

# #呼叫函數
# value=test(3,4)+test(5,10) #(3*4)+(10*5)
# print(value)

#-----程式包裝 ，函數可用來程式包裝:同樣的邏輯可以重複利用
def case(max):         #------縮排表示屬於此迴圈
    sum=0
    for n in range(1,max+1):
        sum=sum+n
    print(sum)      #-----
case(10)
case(20)