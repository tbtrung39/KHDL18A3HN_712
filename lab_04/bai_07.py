a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))

x = a
y = b
while x != y:
    if x < y:
        x += a
    else:
        y += b

print("BCNN là:", x)