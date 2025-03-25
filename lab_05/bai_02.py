#Cach 1:
Str = input("Nhap chuoi: ")
dem = 0
for kt in Str:
    if kt.isalpha() or kt.isdigit():
        dem = 0
    else:
        dem += 1
print("So chu ky khong phai so va khong phai chu cai tieng Anh: ", dem)

#Cach 2:
str = input("Nhap chuoi: ")
count = 0
for i in str:
    if ("0" <= i <= "9") or ("a" <= i <= "z") or ("A" <= i <= "Z"):
        count = 0
    else:
        count += 1
print("So chu ky khong phai so va khong phai chu cai tieng Anh: ", count)
