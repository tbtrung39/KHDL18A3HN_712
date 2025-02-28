n = int(input("Nhập số n: "))
if n < 2:
    print(f"{n} không phải là số nguyên tố")
    la_nguyen_to = False
else:
    la_nguyen_to = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            la_nguyen_to = False
            break

if la_nguyen_to:
    print(f"{n} là số nguyên tố")
else:
    print(f"{n} không phải là số nguyên tố")

    tren= n + 1
    while True:
        la_nguyen_to = True
        for i in range(2, int(tren**0.5) + 1):
            if tren % i == 0:
                la_nguyen_to = False
                break
        if la_nguyen_to:
            break
        tren += 1

    duoi = n - 1
    while duoi > 1:
        la_nguyen_to = True
        for i in range(2, int(duoi**0.5) + 1):
            if duoi % i == 0:
                la_nguyen_to = False
                break
        if la_nguyen_to:
            break
        duoi -= 1

    if n - duoi <= tren - n and duoi > 1:
        print(f"Số nguyên tố gần {n} nhất là {duoi}")
    else:
        print(f"Số nguyên tố gần {n} nhất là {tren}")