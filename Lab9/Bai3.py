#Bai3
def luy_thua(a,n):
    if n==0:
        return 1
    else:
        return a*luy_thua(a,n-1)
a=float(input("Nhập cơ số:"))
n=float(input("Nhập số mũ:"))
kq=luy_thua(a,n)
print(a,"^",n,"=",kq)