a = float(input('Nhập a: '))
b = float(input('Nhập b: '))
c = float(input('Nhập c: '))
x_dinh = -b/(2*a)
y_dinh = a * x_dinh**2 + b * x_dinh + c
print(f'Đỉnh của PTB2 là: ({x_dinh:.2f}, {y_dinh:.2f})')