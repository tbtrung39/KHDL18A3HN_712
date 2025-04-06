#Bai6
#a. Nhập từ bàn phím số tự nhiên n
n = (input("Nhập số tự nhiên n: "))
#b. In ra màn hình dãy n số nguyên tố đầu tiên
ds_so_ngto = []
so_dau_tien = 2
while len(ds_so_ngto) < n:
    so_nguyen_to = True
    if so_dau_tien < 2:
        so_nguyen_to = False
    else:
        for i in range(2, int(so_dau_tien**0.5) + 1):
            if so_dau_tien % i == 0:
                so_nguyen_to = False
                break
    if so_nguyen_to:
        ds_so_ngto.append(so_dau_tien)
    so_dau_tien += 1
print(n, " số nguyên tố đầu tiên là số nguyên tố đầu tiên là:", ds_so_ngto)