def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

n = int(input("Nhập số tự nhiên n: "))
A = {i for i in range(2, n+1) if n % i == 0 and is_prime(i)}
B = {i for i in range(2, n) if is_prime(i) and n % i != 0}

print("Tập A (ước là số nguyên tố của n):", A)
print("Tập B (nguyên tố < n không là ước của n):", B)
