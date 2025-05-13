#a)
def tinh_s_a(n):
    if n == 1:
        return 1 / (1 * 2)
    return 1 / (n * (n + 1)) + tinh_s_a(n - 1)
n = int(input("Nhap n: "))
print("S = ", tinh_s_a(n))

#b)
def tinh_s_b(n):
    if n == 1:
        return 1
    return 1 / tinh_giai_thua(n) + tinh_s_b(n - 1)
def tinh_giai_thua(x):
    if x == 1:
        return 1
    return x * tinh_giai_thua(x - 1)
n = int(input("Nhap n: "))
print("S = ", tinh_s_b(n))

#c)
import math
def tinh_s_c(n):
    if n == 1:
        return math.sqrt(3)
    return math.sqrt(3 * n + tinh_s_c(n - 1))
n = int(input("Nhap n: "))
print("S = ", tinh_s_c(n))

#d)
import math
def tinh_s_d(n):
    if n == 1:
        return math.sqrt(1) ** (1 / (n + 1)) 
    return (n + tinh_s_d(n - 1)) ** (1 / n)

n = int(input("Nhap n: "))
result = tinh_s_d(n)
result = result ** (1 / (n + 1))
print("S = ", result)