def tinh_X(n):
    X = [0] * (n + 1)
    X[0] = 1  
    for i in range(1, n + 1):
        tong = 0
        for k in range(0, i):
            tong += (i - k) ** 2 * X[k]
        X[i] = tong

    return X[n]
for i in range(11):
    print(f"X({i}) = {tinh_X(i)}")
