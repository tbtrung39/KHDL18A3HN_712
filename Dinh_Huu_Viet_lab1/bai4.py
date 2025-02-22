#cau4:
import math
x = float(input("nhap gtri x:"))
fx = ( - x + math.sqrt((x ** 2) + 4)) / (((x**4) + 1) ** (1/7))
print("Giá trị biểu thức là: %0.2f" % fx)