n = int(input("Nhập số nguyên dương n: "))
kq = ""
if n == 0:
    kq = "0"
else:
    while n > 0:
        kq = str(n % 2) + kq
        n //= 2
print("Chuỗi nhị phân là:", kq)
