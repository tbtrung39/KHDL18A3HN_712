#cau4:
import math
x = float(input("nhap gtri x:"))
fx = ( - x + math.sqrt((x ** 2) + 4)) / (((x**4) + 1) ** (1/7))
print("Giá trị biểu thức là: %0.2f" % fx)
#cau5:
a1, a2, a3 = map(int, input("Nhập vector a : ").split())
b1, b2, b3 = map(int, input("Nhập vector b : ").split())
tich_vo_huong = a1*b1 + a2*b2 + a3*b3
print("Tích vô hướng của hai vector:", tich_vo_huong)