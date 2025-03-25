#Cách 1
s = input("Nhập chuỗi kí tự Str là: ")
dem = 0
for c in (s):
    if c.isdigit():
        dem += 1
print("số kí tự là số trong chuỗi là: ",dem)
#Cách 2
s = input("Nhập chuỗi kí tự Str là: ")
dem = 0
for k in (s):
    if "0" <= k <= "9":
        dem += 1
    else:
        0
print("số kí tự là số trong chuỗi là: ",dem)