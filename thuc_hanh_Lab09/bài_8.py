print("cau a \n")
def tong_phan_so(n):
    if n == 1:
        return 1 / (1 * 2)
    return 1 / (n * (n + 1)) + tong_phan_so(n - 1)

n = int(input("Nhập n: "))
print("Tổng S =", tong_phan_so(n))
print("cau b\n")
def tong(n):
    if n == 1:
        return 1
    return 1 / giai_thua(n) + tong(n - 1)
def giai_thua(k):
    if k == 1:
        return 1
    return k * giai_thua(k - 1)
n = int(input("Nhập n: "))
print("Tổng S =", tong(n))

print("cau c\n")
import math
def can_long(n):
    if n == 1:
        return math.sqrt(3)
    return math.sqrt(3 * n + can_long(n - 1))
n = int(input("Nhập n: "))
print("Giá trị S =", can_long(n))
print("cau d\n")
def S(n, k):
    if k == 1:
        return 1 ** (1 / n)
    else:
        return (k - 1 + S(n, k - 1)) ** (1 / n)
n = int(input("Nhập giá trị n (số nguyên dương): "))
ket_qua = S(n + 1, n)
print(f"Kết quả của biểu thức với n = {n} là: {ket_qua}")

