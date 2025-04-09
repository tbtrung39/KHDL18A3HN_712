n = int(input("Nhap so tu nhiên n: "))
A = set()
B = set()
for i in range(2, n):
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break

    if is_prime:
        if n % i == 0:
            A.add(i)
        else:
            B.add(i)

print("Tap hop A (nguyen to la uoc cua n):", A)
print("Tap hop B (nguyen to < n va khong la uoc):", B)