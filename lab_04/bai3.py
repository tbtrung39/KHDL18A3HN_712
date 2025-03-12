x = float(input("Nhập x: "))
n = 1
eps = 10**(-4)
cos_x = 1
a = 1
while abs(a) > eps:
    a *= -x**3 / (n * (n - 1))
    cos_x += a
    n += 2
print("cos(x) =", cos_x)