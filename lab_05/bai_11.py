#Cách 1:
n=input("Nhap chuoi nhi phan: ")
kq=int(n, 2)
print("Chuoi thap phan tuong ung la: ", kq)

#Cách 2:
n=input("Nhap chuoi nhi phan: ")
kq=0
for i in range(len(n)):
    kq=kq*2+int(n[i])
print("So thap phan tuong ung la: ", kq)