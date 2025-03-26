#cach 1 
s=input("nhap chuoi nhi phan: ")
kq=int(s, 2)
print("ket qua thap phan:", kq)
#cach 2
s=input("nhap chuoi nhi phan: ")
kq=0
for i in range(len(s)):
    kq=kq*2+int(s[i])
print("ket qua thap phan:", kq)