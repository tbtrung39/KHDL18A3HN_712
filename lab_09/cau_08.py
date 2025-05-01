#a
def tinh_S_a(n):
    if n == 1:
        return 1 / (1 * 2)
    return 1 / (n * (n + 1)) + tinh_S_a(n - 1)

#b
def tinh_S_b(n):
    if n == 1:
        return 1
    return 1 / tinh_giai_thua(n) + tinh_S_b(n - 1)

def tinh_giai_thua(n):
    if n == 1:
        return 1
    return n * tinh_giai_thua(n - 1)

#c
import math

def tinh_S_c(n):
    if n == 1:
        return math.sqrt(3)
    return math.sqrt(3 * n + tinh_S_c(n - 1))

#d
def tinh_S_d(n, k=1):
    if k == n - 1:
        return (2 + 1**0.5) ** (1 / n)  # tầng gần cuối: sqrt[n]{2 + √1}
    if k == n:
        return (n - 1 + tinh_S_d(n, k - 1)) ** (1 / n)  # tầng n: sqrt[n]{...}
    if k > n:
        return (n + tinh_S_d(n, n)) ** (1 / (n + 1))  # tầng đầu: sqrt[n+1]{...}
    return (n - k + tinh_S_d(n, k + 1)) ** (1 / n)  # các tầng còn lại

#######
n = int(input("Nhập n: "))
print("S_a =", tinh_S_a(n))
print("S_b =", tinh_S_b(n))
print("S_c =", tinh_S_c(n))
print("S_d =", tinh_S_d(n, n + 1))