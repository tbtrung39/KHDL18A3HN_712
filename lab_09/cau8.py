# Câu a
def tinh_sa(n):
    if n == 1:
        return 1 / (1 * 2)
    return 1 / (n * (n + 1)) + tinh_sa(n - 1)
n = int(input("Nhap n: "))
print("S = ", tinh_sa(n))
# Câu b
def tinh_b(n):
    if n == 1:
        return 1
    return 1 / tinh_giai_thua(n) + tinh_b(n - 1)
def tinh_giai_thua(x):
    if x == 1:
        return 1
    return x * tinh_giai_thua(x - 1)
n = int(input("Nhap n tu ban phim: "))
print("S = ", tinh_b(n))
# Câu c
import math
def tinh_c(n):
    if n == 1:
        return math.sqrt(3)
    return math.sqrt(3 * n + tinh_c(n - 1))
n = int(input("Nhap n tu ban phim: "))
print("S = ", tinh_c(n))
# Câu d
import math
def tinh_d(n):
    if n == 1:
        return math.sqrt(1) ** (1 / (n + 1)) 
    return (n + tinh_d(n - 1)) ** (1 / n)
n = int(input("Nhap n tu ban phim: "))
result = tinh_d(n)
result = result ** (1 / (n + 1))
print("S = ", result)