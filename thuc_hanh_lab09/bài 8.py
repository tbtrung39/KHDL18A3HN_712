def cau_a(n):
    if n == 1:
        return 1 / (1 * 2)
    return 1 / (n * (n + 1)) + cau_a(n - 1)
n = int(input("Nhap n: "))
print("S = ", cau_a(n))
def cau_b(n):
    if n == 1:
        return 1
    return 1 / tinh_giai_thua(n) + cau_b(n - 1)
def tinh_giai_thua(x):
    if x == 1:
        return 1
    return x * tinh_giai_thua(x - 1)
n = int(input("Nhap n tu ban phim: "))
print("S = ", cau_b(n))
import math
def cau_c(n):
    if n == 1:
        return math.sqrt(3)
    return math.sqrt(3 * n + cau_c(n - 1))
n = int(input("Nhap n tu ban phim: "))
print("S = ", cau_c(n))
import math
def cau_d(n):
    if n == 1:
        return math.sqrt(1) ** (1 / (n + 1)) 
    return (n + cau_d(n - 1)) ** (1 / n)
n = int(input("Nhap n tu ban phim: "))
result = cau_d(n)
result = result ** (1 / (n + 1))
print("S = ", result)