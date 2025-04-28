def tinh_X(n, X={0: 1}):
    if n in X:
        return X[n]
    X_n = 0
    for i in range(n):
        X_n += (n - i) ** 2 * tinh_X(i, X)
    X[n] = X_n  
    return X_n
n = int(input("Nhập số n: "))
print("X^n = ", tinh_X(n))