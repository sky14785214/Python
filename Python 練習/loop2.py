#break 強制結束迴圈
#continue 強制執行下一圈
#else 迴圈結束前，執行此區塊命令

#------
#n=1
#while n<5:
#    if n==3:
#        break
#    n=n+1
#print(n)
#當n倍加到3時執行break 強行跳出整個while
#----------
# n=0
# for x in range(0,4): #range(0,4)=[0,1,2,3]
#    if x%2==0:
#        continue
#    n+=1
# print(n)
# 0-4 數字除以2當餘數=0，執行continue 跳過n+=1，繼續執行迴圈
# 答案n=2，因為1和3皆不能整除 所以會n會加2次
#-----------
#else
# sum=0
# for n in range(11):
#     sum=sum+n
# else:
#     print(sum)
#------------
#整數平方根
#輸入9 得到3
#輸入11 得到[沒有] 整數平方根
n=input("請入一個正整數: ") 
n=int(n) #轉換輸入成數字
for i in range(n): # i從0~n-1
    if i*i==n:      # 將輸入的值-1 從0開始平方 若等於輸入值n就是他的平方根
        print("整數平方根",i)
        break       #用break強制結束迴圈 就不會執行else
else:
     print("沒有整數平方根")
