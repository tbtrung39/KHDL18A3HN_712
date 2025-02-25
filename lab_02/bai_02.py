from math import *
a = float(input('Nhập a: '))
b = float(input('Nhập b: '))
c = float(input('Nhập c: '))
if a == 0:
    if b == 0:
        if c == 0:
            print('Phương trình vô số nghiệm. ')
        else:
            print('Phương trình vô nghiệm. ')
    else:
        print(f'Phương trình có nghiệm x = {-c / b}')
else:
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + sqrt(delta)) / (2*a)
        x2 = (-b - sqrt(delta)) / (2*a)
        print(f'Phương trình có 2 nghiệm phân biệt: x1 = {x1}, x2 = {x2}')
    elif delta == 0:
        x = -b / (2*a)
        print(f'Phương trình có nghiệm kép x1 = x2 = {x}')
    else:
        print('Phương trình vô nghiệm')
