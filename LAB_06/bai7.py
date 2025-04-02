n = int(input("Nhap so phan tu: "))
a = [(int(input(f"Nhap phan tu thu {i + 1}: ")), i) for i in range(n)]
prime_numbers = [x for x in a if x[0] > 1 and all(x[0] % i != 0 for i in range(2, int(x[0]**0.5) + 1))]
if prime_numbers:
    max_prime, max_prime_pos = max(prime_numbers, key=lambda x: x[0])
    print("So nguyen to lon nhat:", max_prime, "o vi tri", max_prime_pos)
else:
    print("Khong co so nguyen to trong danh sach")
