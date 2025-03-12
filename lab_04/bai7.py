a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
a1, b1 = a, b
while b1:
    a1, b1 = b1, a1 % b1
gcd = a1
lcm = (a * b) // gcd
print("BCNN =", lcm)