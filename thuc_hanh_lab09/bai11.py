def tinh_giai_thua_kep(n):
    if n==0 or n==1:
        return 1
    return n*tinh_giai_thua_kep(n-2)
def tinh_tong(m):
    tong=0
    for i in range (1, m+1):
        tong+= ((-1)**i)*tinh_giai_thua_kep(i)
        return tong
m=int(input("nhap m:"))
print("tong cua s la:", tinh_tong(m))
