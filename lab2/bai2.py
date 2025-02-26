print("Chương trình giải phương trình bậc hai ax^2 + bx + c = 0")
print("Nhập a:", end=" ")
a = float(input())
print("Nhập b:", end=" ")
b = float(input())
print("Nhập c:", end=" ")
c = float(input())
if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình có vô số nghiệm.")
        else:
            print("Phương trình vô nghiệm.")
    else:
        x = -c / b
        print("Phương trình có một nghiệm x =", x)
else:
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + delta**0.5) / (2*a)
        x2 = (-b - delta**0.5) / (2*a)
        print("Phương trình có hai nghiệm phân biệt:")
        print("x1 =", x1)
        print("x2 =", x2)
    elif delta == 0:
        x = -b / (2*a)
        print("Phương trình có nghiệm kép x =", x)
    else:
        print("Phương trình vô nghiệm.")
