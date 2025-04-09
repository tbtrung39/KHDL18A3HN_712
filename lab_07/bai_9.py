n = int(input("Hay nhap so tu nhien n=: "))
A = set()
B = set()
so = 2
while so <= n:
    la_so_nguyen_to = True

    i = 2
    while i < so:
        if so % i == 0:
            la_so_nguyen_to = False
            break
        i += 1

    if la_so_nguyen_to:
        if n % so == 0:
            A.add(so)   
        elif so < n:
            B.add(so)   
    so += 1
print("Tập hợp A (ước nguyên tố của", n, "):", A)
print("Tập hợp B (nguyên tố nhỏ hơn", n, "nhưng không là ước):", B)