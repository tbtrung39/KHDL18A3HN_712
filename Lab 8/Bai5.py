#Bai5
def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
print("UCLN của", a, "và", b, "là:", ucln(a, b))