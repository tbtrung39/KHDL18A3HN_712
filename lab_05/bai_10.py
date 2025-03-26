str1=input("Nhap chuoi 1: ")
str2=input("Nhap chuoi 2: ")
max=""
for i in range(len(str1)):
    for j in range(i+1, len(str1)+1):
        kt=str1[i:j]
        if kt in str2 and len(kt)>len(max):
            max=kt
if max:
    print("Chuoi con chung dai nhat la:", max)
else:
    print("Khong co chuoi con chung nao.")