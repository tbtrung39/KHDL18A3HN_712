# Nhập n sao cho n > 0
n = int(input("Nhập n (số nguyên dương): "))
while n <= 0:
    n = int(input("Nhập lại n (số nguyên dương): "))

# a) S4 = 1^2 + 2^2 + ... + n^2
S4 = 0
i = 1
while i <= n:
    S4 += i ** 2
    i += 1
print("S4 =", S4)

# b) S5 = 1^3 + 3^3 + ... + (2n+1)^3
S5 = 0
i = 1
while i <= (2 * n + 1):
    S5 += i ** 3
    i += 2
print("S5 =", S5)

# c) S6 = 2^4 + 4^4 + ... + (2n)^4
S6 = 0
i = 2
while i <= 2 * n:
    S6 += i ** 4
    i += 2
print("S6 =", S6)