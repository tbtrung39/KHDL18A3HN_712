import math
r = float(input('Nhập bán kính: '))
h = float(input('Nhập chiều cao: '))
dt_xq = 2 *  math.pi * r * h
dt_tp = 2 *  math.pi * r * (r + h)
v =  math.pi * r**2 * h
print(f'Diện tích xung quanh: {dt_xq:.2f}')
print(f'Diện tích toàn phần: {dt_tp:.2f}')
print(f'Thể tích: {v:.2f}')