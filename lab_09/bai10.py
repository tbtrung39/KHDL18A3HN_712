def tinh_X(n, X={0: 1}):
    if n in X:
        return X[n]
    
    X_n = 0
    for i in range(n):
        X_n += (n - i) ** 2 * tinh_X(i, X)
    X[n] = X_n  
    return X_n

n = int(input("hay nhap n tu ban phim: "))
print("kq cua bai toan la = ", tinh_X(n))