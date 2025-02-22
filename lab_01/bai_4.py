x = float(input("Nhập giá trị x: "))
fx = (-x + (x**2 + 4) ** (1/2)) / ((x**4 + 1) ** (1/7))
fx = round(fx, 2)  # làm tròn
print("Giá trị của f(x) là:", fx)