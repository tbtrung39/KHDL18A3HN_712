def luu_thua(a, n):
    if n == 0:
        return 1
    elif n > 0:
        return a * luu_thua(a, n - 1)
    else:
        return 1 / luu_thua(a, -n)
a = float(input("Nhập cơ sở a: "))
n = int(input("Nhập số mũ n: "))

result = luu_thua(a, n)
print(f"Kết quả của {a}^{n} là: {result}")