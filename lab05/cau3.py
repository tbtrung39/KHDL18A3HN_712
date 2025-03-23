
n=int(input("nhap số nguyên dương n: "))
kq=""
if n==0:
    kq="0"
else:
    while n>0:
        kq=str(n%2)+kq
        n=n//2
print("chuỗi nhị phân là:", kq)
