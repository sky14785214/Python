#載入內建sys模組並取得資訊
# import sys as system             # 模組 as 別名(代號)
# print(system.platform)
# print(system.maxsize)


#調整模組搜尋路徑
import sys
#print(sys.path) # 印出模組的搜尋路徑
sys.path.append("modules")      #當前路徑(相對路徑)下的搜尋路徑
#建立 geometry.py，載入使用
import geometry
result=geometry.distance(1,1,5,5)   # geometry.distance 模組中函數名稱
print(result)
result=geometry.slope(1,2,5,6)      #geometry.distance
print(result)

