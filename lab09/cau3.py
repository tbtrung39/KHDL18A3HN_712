def luy_thua(a,n):
    if n==0:
        return 1
    return a*luy_thua(a,n-1)

a=int(input("nhap co so: "))
n=int(input("nhap so mu: "))
if n<0:
    print("so mu phai lon hon 0: ")
else:
    kq= luy_thua(a,n)
    print(f"{a}^{n}={kq}")