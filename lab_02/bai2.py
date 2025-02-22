a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
if a == 0:
    print("Không phải phương trình bậc hai.")
else:
    delta = b*b - 4*a*c
    if delta > 0:
        x1 = (-b + (delta)**0.5) / (2*a)
        x2 = (-b - (delta)**0.5) / (2*a)
        print("Phương trình có 2 nghiệm:", x1, "và", x2)
    elif delta == 0:
        x = -b / (2*a)
        print("Phương trình có nghiệm kép:", x)
    else:
        print("Phương trình vô nghiệm.")
