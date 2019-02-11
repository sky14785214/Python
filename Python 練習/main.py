#主程式
import geometry.point
result=geometry.point.distance(3,4)
print(result)

import geometry.line as line # 可as加別名 往後程式都用別名可縮減程式長度
result=line.slope(1,1,3,3)
print("斜率",result)