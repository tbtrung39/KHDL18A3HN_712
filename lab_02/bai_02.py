#cau2:
import math
a = int(input("Nhập vào số a: "))
b = int(input("Nhập vào số b: "))
c = int(input("Nhập vào số c: "))
delta = b**2 - 4*a*c
if delta < 0:
    print("Phương trình vô nghiệm")
elif delta == 0:
    x = -b / (2 * a)
    print("Phương trình có nghiệm kép x =", x)
else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print("Phương trình có 2 nghiệm phân biệt:")
    print("x1 =", x1)
    print("x2 =", x2)