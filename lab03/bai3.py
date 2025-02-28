import math
n = int(input("Nhập số n: "))
nguyen_to = True
if n < 2:
    nguyen_to = False
for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
        nguyen_to = False
        break
if nguyen_to:
    print(f"{n} là số nguyên tố.")
else:
    so_nguyen_to_duoi = 0
    so_nguyen_to_tren = 0
    
    for i in range(n - 1, 1, -1):
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                break
        else:
            so_nguyen_to_duoi = i
            break
    for i in range(n + 1, n * 2):
        la_nguyen_to = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                break
        else:
            so_nguyen_to_tren = i
            break
    if n-so_nguyen_to_duoi<=so_nguyen_to_tren-n:
        print(f"{n} không phải là số nguyên tố. Số nguyên tố gần nhất là {so_nguyen_to_duoi}.")
    else:
        print(f"{n} không phải là số nguyên tố. Số nguyên tố gần nhất là {so_nguyen_to_tren}.")
