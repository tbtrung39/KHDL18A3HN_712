def giai_thua_kep(n):
    if n == 0 or n == 1:
        return 1
    return giai_thua_kep(n - 2) * n

def tinh_tong(k):
    tong = 0
    for i in range(1, k + 1):
        tong += (-1)**(i + 1) * giai_thua_kep(i)
    return tong

k = int(input("Nhập k (k < 1000): "))
if k < 1000:
    print("Tổng S =", tinh_tong(k))
else:
    print("Giá trị k không hợp lệ. k phải nhỏ hơn 1000.")
