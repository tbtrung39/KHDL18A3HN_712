n = int(input("Nhap so tu nhien n: "))
A = set()
B = set()
for i in range(2, n):
    so_nt = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            so_nt = False
            break
    if so_nt:
        if n % i == 0:
            A.add(i)
        else:
            B.add(i)
print("Tap hop A: ", A)
print("Tap hop B: ", B)