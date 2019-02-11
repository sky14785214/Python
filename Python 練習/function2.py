# def 函式名稱(參數名稱=預設資料)
#   函式內部程式碼

# def 函式名稱(名稱1,名稱2):
#     函式內部程式碼
## 呼叫
# 函式名稱(名稱2=3,名稱1=5)
# def test(n1,n2):
#     a=n1/n2
#     print(a)
# test(2,4)
# test(n2=2,n1=4)
#------
#無限長度的參數
# def 函數名稱(*無限參數): *號就是以無限參數以tuple資料型態處理
#     函式內部的程式碼
# 呼叫
# 函數名稱(資料一,資料二,資料三)
#------
# def say(*msgs):
#     for msg in msgs: #利用列表方式tuple存取資料
#         print(msg)
# say("hello","say","nice")
#-------
#參數預設資料
# def power(base,exp=0): #exp=0是賦予0次方
#     print(base**exp)    #a**b是a的b次方
# power(3,2)
#----
#使用參數名稱
# def divide(n1,n2):
#     print(n1/n2)
# divide(4,2)
# divide(n1=2,n2=4)
#------
#無限/不定參數資料
def avg(*num):   #*不定長度的資料
    sum=0
    for n in num:
        sum=sum+n
    print(sum/len(num)) #len列表長度

avg(3,4)
avg(3,5,10)
avg(1,4,-1,-8)
