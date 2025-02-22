from math import *
a = float(input('Nhập vận tốc ban đầu của ô tô: '))
log4_5 = log(5) / log(4)
t = (a ** 4) / log4_5
print(f'Thời gian ô tô dừng lại: {t:.2f} giây')
