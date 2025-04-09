n = int(input("Nhap so tu nhien n: "))
a = set()
b = set()
for i in range(2, n):
    so_nt = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            so_nt = False
            break
    if so_nt:
        if n % i == 0:
            a.add(i)
        else:
            b.add(i)
print("Tap hop a: ", a)
print("Tap hop b: ", b)