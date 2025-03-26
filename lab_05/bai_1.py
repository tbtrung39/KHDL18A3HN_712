# Cách 1
Str = input("Nhap chuoi ky tu: ")
a = 0
for i in Str:
    if i.isdigit():
        a += 1
print("So cac ky tu trong Str la: ", a)

#Cách 2
str = input("Nhap chuoi ky tu: ")
b = 0
for j in str:
    b += 1 if '0' <= j <= '9' else 0
print("So cac ky tu trong str la: ", b)