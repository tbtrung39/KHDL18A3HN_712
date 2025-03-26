#Cách 1
str = input("Nhap chuoi ky tu: ")
a = 0
for i in str:
    if not (i.isalpha() or i.isdigit()):
        a+=1
print("So ky tu khong phai la chu cai tieng Anh va khong phai la so trong chuoi str la: ", a)

#Cach 2
str = input("Nhap chuoi ky tu: ")
b = 0
for j in str:
    ma=ord(j)
    if not (48<=ma<=57 or 65<=ma<=90 or 97<=ma<=122):
        b+=1
print("So ky tu khong phai la chu cai tieng Anh va khong phai la so trong chuoi str la:", b)