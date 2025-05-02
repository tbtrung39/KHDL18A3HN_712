def luu_thua(a, n):
    if n == 0:
        return 1
    return a * luu_thua(a, n - 1)

a = int(input("Nhap co so a: "))
n = int(input("Nhap so mu n: "))
if n < 0:
    print("So mu phai > 0!!!")
else:
    kq = luu_thua(a, n)
    print(f"{a}^{n} = {kq}")