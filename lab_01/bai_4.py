import math

def f(x):
    tu_so = -x + ((x**2 + 4)**(1/2))
    mau_so = (x**4 + 1)**(1/7)
    return round(tu_so / mau_so, 2)

x = float(input("Nhập giá trị x: "))
print(f"Giá trị của f({x}) là: {f(x)}")
