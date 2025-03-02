n = int(input("Nhập n: "))
nguyen_to = True
if n < 2:
    nguyen_to = False
else:
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            nguyen_to = False
            break
import math 
if nguyen_to:
    print(f"{n} là số nguyên tố.")
else:
    duoi, tren = n - 1, n + 1
    while True:
        if duoi > 1:
            for i in range(2, int(math.sqrt(duoi)) + 1):
                if duoi % i == 0:
                    duoi -= 1
                    break
            else:
                break
        else:
            break
    while True:
        for i in range(2, int(math.sqrt(tren)) + 1):
            if tren % i == 0:
                tren += 1
                break
        else:
            break
    print(f"{n} không phải số nguyên tố. Số nguyên tố gần nhất là {duoi} hoặc {tren}.")
