n = int(input("Nhập n: "))

la_nguyen_to = True
if n < 2:
    la_nguyen_to = False
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            la_nguyen_to = False
            break

if la_nguyen_to:
    print(f"{n} là số nguyên tố")
else:
    khoang_cach = 1
    while True:
        if n - khoang_cach >= 2:
            so_trai = n - khoang_cach
            la_nguyen_to = True
            for i in range(2, int(so_trai ** 0.5) + 1):
                if so_trai % i == 0:
                    la_nguyen_to = False
                    break
            if la_nguyen_to:
                print(f"{n} không phải là số nguyên tố")
                print(f"Số nguyên tố gần {n} nhất là: {so_trai}")
                break

        so_phai = n + khoang_cach
        la_nguyen_to = True
        for i in range(2, int(so_phai ** 0.5) + 1):
            if so_phai % i == 0:
                la_nguyen_to = False
                break
        if la_nguyen_to:
            print(f"{n} không phải là số nguyên tố")
            print(f"Số nguyên tố gần {n} nhất là: {so_phai}")
            break
            
        khoang_cach += 1