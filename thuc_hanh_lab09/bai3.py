def tinh_luy_thua(a,n):
    if n==0:
        return 1
    else:
        return a*tinh_luy_thua(a,n-1)
a=float(input("nhap co so:"))
n=float(input("nhap so mu:"))
kq=tinh_luy_thua(a,n)
print(a,"^",n,"=",kq)