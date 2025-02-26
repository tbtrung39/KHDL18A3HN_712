#Bai2
import math
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
if a==0:
    if b==0:
        if c==0:
            print("Phương trình có vô số nghiệm.")
        else:
            print("Phương trình vô nghiệm.")
    else:
        x=-c/b
        print("Phương trình có một nghiệm:", x)
else:
    delta=b**2-4*a*c
    if delta<0:
        print("Phương trình vô nghiệm.")
    elif delta==0:
        x=-b/(2*a)
        print("Phương trình có nghiệm kép:", x)
    else:
        x1=(-b+math.sqrt(delta))/(2*a)
        x2=(-b-math.sqrt(delta))/(2*a)
        print("Phương trình có hai nghiệm phân biệt:")
        print("x1 =", x1)
        print("x2 =", x2)