import math
x = float(input("Nhập giá trị x: "))

f_x = (-x + math.sqrt(x**2 + 4)) / (7 * math.sqrt(x**4 + 1))
f_x = round(f_x, 2)

print(f"Giá trị của biểu thức f(x): {f_x}")