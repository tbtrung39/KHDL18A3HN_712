while True:
    x = input("Nhập số nguyên thứ nhất: ")
    i = 0
    while i < len(x) and (x[i] == "-" or "0" <= x[i] <= "9"):
        i += 1
    if i == len(x) and x != "-":
        x = int(x)
        break

while True:
    y = input("Nhập số nguyên thứ hai: ")
    i = 0
    while i < len(y) and (y[i] == "-" or "0" <= y[i] <= "9"):
        i += 1
    if i == len(y) and y != "-":
        y = int(y)
        break

a, b = x, y
while b:
    a, b = b, a % b

print("BCNN là:", abs(x * y) // a)
