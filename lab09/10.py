def X(n):
    if n == 0:
        return 1
    tong = 0
    for i in range(n):
        tong += ((n - i) ** 2) * X(i)
    return tong
print("Xn =", X(4))
