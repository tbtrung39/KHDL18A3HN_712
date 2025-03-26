#Bai12
#Cách 1
print("Cách 1: ")
str1 = input("Nhập chuỗi ký tự: ")
str1 = str1.replace(',', ' ') 
ds_tu = str1.split() 
for tu in ds_tu:
    print(tu)
#Cách 2
print("Cách 2: ")
s = input("Nhập chuỗi ký tự: ")
chuoi_tam_thoi = ' '
for ky_tu in s:
    if ky_tu == ",": 
        chuoi_tam_thoi += " "
    else:
        chuoi_tam_thoi += ky_tu
ds_tu = chuoi_tam_thoi.split() 
for tu in ds_tu:
    print(tu)