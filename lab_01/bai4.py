from math import *
x = float(input('Nhập x: '))
f_x = (-x + sqrt(x**2 + 4)) / ((x**4 + 1)**(1/7))
print(f'Giá trị của biểu thức: {f_x:.2f}')
