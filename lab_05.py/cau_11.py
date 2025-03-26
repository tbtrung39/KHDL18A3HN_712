#1
s=input("nhập chuỗi nhi phân: ")
kq=int(s, 2)
print("kết quả thập phân là:", kq)
#2
s=input("nhập chuỗi nhị phân: ")
kq=0
for i in range(len(s)):
    kq=kq*2+int(s[i])
print("kết quả thập phân phân là:", kq)