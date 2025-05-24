def X(n):
    if n==0: return 1
    return sum((n-k)**2*X(k) for k in range(n))
n=int(input("Nhập n:"))
print(f"X({n})={X(n)}")
