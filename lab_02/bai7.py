a1 = float(input("Nhập a1: "))
b1 = float(input("Nhập b1: "))
c1 = float(input("Nhập c1: "))
a2 = float(input("Nhập a2: "))
b2 = float(input("Nhập b2: "))
c2 = float(input("Nhập c2: "))
D = a1 * b2 - a2 * b1
Dx = c1 * b2 - c2 * b1
Dy = a1 * c2 - a2 * c1
if D != 0:
    x = Dx / D
    y = Dy / D
    print(f"Giải hệ phương trình: x = {x}, y = {y}")
else:
    print("Hệ phương trình vô nghiệm hoặc có vô số nghiệm.")
