n = int(input("Nhập n: "))  
kiem_tra_so_nguyen_to = True  
if n < 2:
    kiem_tra_so_nguyen_to = False
else:
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:
            kiem_tra_so_nguyen_to = False
            break
if kiem_tra_so_nguyen_to:
    print(n, "là số nguyên tố")
else:
    so_nho_hon = n - 1  
    so_lon_hon = n + 1  
    while True:
        kiem_tra_so_nguyen_to_nho_hon = True
        kiem_tra_so_nguyen_to_lon_hon = True
        if so_nho_hon >= 2:
            for i in range(2, int(so_nho_hon**0.5) + 1):
                if so_nho_hon % i == 0:
                    kiem_tra_so_nguyen_to_nho_hon = False
                    break
        else:
            kiem_tra_so_nguyen_to_nho_hon = False
        for i in range(2, int(so_lon_hon**0.5) + 1):
            if so_lon_hon % i == 0:
                kiem_tra_so_nguyen_to_lon_hon = False
                break
        if kiem_tra_so_nguyen_to_nho_hon:
            print("Số nguyên tố gần nhất:", so_nho_hon)
            break
        if kiem_tra_so_nguyen_to_lon_hon:
            print("Số nguyên tố gần nhất:", so_lon_hon)
            break
        so_nho_hon -= 1
        so_lon_hon += 1
