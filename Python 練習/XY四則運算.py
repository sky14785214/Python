X=int(input("請輸入X值: "))
Y=int(input("請輸入Y值: "))
Z=input("請輸入+，-，*，/: ")

if Z=="+":
    print(X+Y)
elif    Z=="-":
    print(X-Y)
elif    Z=="*":
    print(X*Y)
elif    Z=="/":
    print(X/Y)
else:
    print("無效輸入")