x = float(input("Nhập x: "))
epsilon = 10**-4
cos_x = 1
term = 1
i = 1

while abs(term) > epsilon:
    term *= -x**2 / ((2*i-1) * (2*i))
    cos_x += term
    i += 1

print("cos(x) ≈", cos_x)