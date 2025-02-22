# bài 2
import math
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình có vô số nghiệm.")
        else:
            print("Phương trình vô nghiệm.")
    else:
        x = -c / b
        print("Phương trình có nghiệm duy nhất: x =", x)
else:
    b2 = b * b
    ac4 = 4 * a * c
    if b2 < ac4:
        print("Phương trình vô nghiệm.")
    elif b2 == ac4:
        x = -b / (2 * a)
        print("Phương trình có nghiệm kép: x =", x)
    else:
        can_b2_ac4 = math.sqrt(b2 - ac4)
        x1 = (-b + can_b2_ac4) / (2 * a)
        x2 = (-b - can_b2_ac4) / (2 * a)
        print("Phương trình có hai nghiệm phân biệt: x1 =", x1, ", x2 =", x2)
