def luy_thua(a, n):
    if n == 0:
        return 1
    else:
        return a * luy_thua(a, n-1)
a = float(input("Nhap co so a: "))
n = int(input("Nhap so mu n: "))
kq = luy_thua(a, n)
print("Ket qua cua", a, "^", n, "la:", kq)