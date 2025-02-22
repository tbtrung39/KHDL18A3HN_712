#Bài 4
import math
x = float(input("Nhập giá trị x: "))
fx = (-x + math.sqrt(x**2 + 4)) / (7 * math.sqrt(x**4 + 1))
fx = round(fx, 2)
print(f"Giá trị của f(x) là: {fx}")