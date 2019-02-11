#定義類別 與 類別屬性(封裝在類別中的變數和函式)
#定義一個類別IO,兩個屬性 supporetesSrcs 和 read
# class IO:
#     supportesSrcs=["console","file"]
#     def read(src):
#         print("Read form",src)
# #使用類別
# print(IO.supportesSrcs)
# IO.read("file")
#------
class IO:
    supportesSrcs=["console","file"]
    def read(src):
        if src not in IO.supportesSrcs:
            print("not supportesSrcs")
        else:
            print("Read form",src)
#使用類別
print(IO.supportesSrcs)
IO.read("file")
IO.read("internet")