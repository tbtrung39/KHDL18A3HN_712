import math
x = float(input("Nhập giá trị x (radian): "))
cos_x = 1 
term = 1
n = 1
while abs(term) > 1e-4:
    term *= -x**2 / (n * (n + 1))
    cos_x += term
    n += 2
print(f"Giá trị gần đúng của cos({x}) là: {cos_x}")
print(f"Giá trị thực tế của cos({x}) là: {math.cos(x)}")