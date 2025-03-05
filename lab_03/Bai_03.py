n = int(input('Nhập vào số n: '))
t = 0
for i in range(1, n + 1):
    if n % i == 0:
        t += 1
if t == 2:
    print(f'{n} là số nguyên tố')
else:
    print(f'{n} không phải là số nguyên tố')
    so_nguyen_to_duoi = 0 
    for i in range(n - 1, 1, -1):
        t = 0
        for j in range(1, i + 1):
            if i % j == 0:
                t += 1
        if t == 2:
            so_nguyen_to_duoi = i
            break
    
    so_nguyen_to_tren = 0
    for i in range(n + 1, 1000000):
        t = 0
        for j in range(1, i + 1):
            if i % j == 0:
                t += 1
        if t == 2:
            so_nguyen_to_tren = i
            break
    if n - so_nguyen_to_duoi < so_nguyen_to_tren - n:
        print(f'Số nguyên tố dưới gần với {n} nhất là {so_nguyen_to_duoi}')
    else:
        print(f'Số nguyên tố trên gần với {n} nhất là {so_nguyen_to_tren}')
    