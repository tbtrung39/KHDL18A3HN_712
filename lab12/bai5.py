def tinh_s1(n):
    return sum(range(1, n + 1))

def tinh_s2(n):
    return sum(i ** 2 for i in range(1, n + 1))

try:
    n = int(input("nhap n: "))
    if n <= 0:
        print("n phai lon hon 0")
    else:
        print("s1 =", tinh_s1(n))
        print("s2 =", tinh_s2(n))
except ValueError:
    print("loi, n khong phai so nguyen")