so = int(input("Nhập vào một số nguyên dương: "))
if so < 2:
    print("Số nhập vào không hợp lệ")
else:
    la_so_dau = True 
    for i in range(2, so + 1):
        for j in range(so):
            if so % i == 0:
                if la_so_dau:
                    print(i, end="")
                    la_so_dau = False
                else:
                    print(" *", i, end="")
                so = so // i
            else:
                break 