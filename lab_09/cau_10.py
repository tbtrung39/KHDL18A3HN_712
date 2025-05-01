def X(n):
    if n == 0:
        return 1
    return sum((n - i) ** 2 * X(i) for i in range(n))

n = int(input("Nhập n: "))
print(f"X_{n} =", X(n))
