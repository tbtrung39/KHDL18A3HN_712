def luu_thua(a, n):
    if n == 0:
        return 1
    elif n > 0:
        return a * luu_thua(a, n-1)
    else:
        return 1 / luu_thua(a, -n)
a = float(input("Nhap co so a: "))
n = int(input("Nhap so mu n: "))

result = luu_thua(a, n)
print(f"Ket qua cua {a}^{n} la: {result}")