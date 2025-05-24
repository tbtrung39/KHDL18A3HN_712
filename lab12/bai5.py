def S1(n):
    if n < 1:
        raise ValueError("n phai >= 1")
    if n == 1:
        return 1
    return n + S1(n - 1)

def S2(n):
    if n < 1:
        raise ValueError("n phai >= 1")
    if n == 1:
        return 1
    return n**2 + S2(n - 1)

try:
    n = int(input("Nhap n: "))
    print("S1 =", S1(n))
    print("S2 =", S2(n))
except ValueError as e:
    print("Loi:", e)

