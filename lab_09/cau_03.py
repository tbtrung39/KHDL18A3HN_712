def luy_thua(a, n):
    return 1 if n == 0 else a * luy_thua(a, n - 1)

a = int(input("Nhập cơ số a: "))
n = int(input("Nhập số mũ n: "))
print(f"{a}^{n} =", luy_thua(a, n))
