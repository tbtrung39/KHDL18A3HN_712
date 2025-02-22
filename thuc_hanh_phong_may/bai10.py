import math
x = float(input("Nhập giá trị x: "))
f_x = math.log(x) / math.log(4) + math.log(2) / math.log(x)
print("Giá trị của f(x) là:", round(f_x, 2))
