import math
x = float(input("Nhập giá trị x: "))

f_x = math.log(x, 4) + math.log(2, x)
f_x = round(f_x, 2)

print(f"Giá trị của biểu thức f(x): {f_x}")
