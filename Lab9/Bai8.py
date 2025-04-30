#Bai8
import math
#a
def tong_a(n):
    if n == 1:
        return 1 / (1 * 2)
    return 1 / (n * (n + 1)) + tong_a(n - 1)
#b
def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    return n * giai_thua(n - 1)
def tong_b(n):
    if n == 1:
        return 1 / 1
    return 1 / giai_thua(n) + tong_b(n - 1)
#c
def tong_c(n):
    if n == 1:
        return math.sqrt(3)
    return math.sqrt(3 * n + tong_c(n - 1))
#d
def tong_d(n):
    if n == 1:
        return math.sqrt(1)
    return math.sqrt(n + tong_d(n - 1))
n = int(input("Nhập n: "))
print("Tổng a là S=", tong_a(n))
print("Tổng b là S=", tong_b(n))
print("Tổng c là S=", tong_c(n))
print("Tổng d là S=", tong_d(n))