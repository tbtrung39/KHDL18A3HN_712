def tinh_s1(n):
    return sum(range(1, n + 1))

def tinh_s2(n):
    return sum(i ** 2 for i in range(1, n + 1))

try:
    n = int(input("Nhap n: "))
    if n <= 0:
        print("Dieu kien n > 0")
    else:
        print("S1 =", tinh_s1(n))
        print("S2 =", tinh_s2(n))
except ValueError:
    print("Loi, n khong phai so nguyen!!!")