def giai_thua_kep(n):
    if n == 0 or n == 1:
        return 1
    return giai_thua_kep(n - 2) * n

def tinh_tong(k):
    tong = 0
    for i in range(1, k + 1):
        if i % 2 == 1:
            tong += giai_thua_kep(i)
        else:  
            tong -= giai_thua_kep(i)
    return tong
k = int(input("Nhap gia tri k nho hon 1000: "))
print("Tong S = ", tinh_tong(k))