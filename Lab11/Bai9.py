def xu_ly_hanh_khach():
    with open('PASSENGERS.IN', 'r') as file:
        lines = [line.strip() for line in file if line.strip()]
    so_hanh_khach = int(lines[0])
    do_sach_tay = [list(map(float, line.split())) for line in lines[1:1 + so_hanh_khach]]
    tong_trong_luong = []
    huy_chuyen = []
    for so_luong, ds_do in enumerate(do_sach_tay):
        tong = sum(ds_do)
        tong_trong_luong.append(tong)
        if tong > 23 or len(ds_do) > 5:
            huy_chuyen.append(str(so_luong + 1))
    with open('WEIGHT.OUT', 'w') as file:
        for trong_luong in tong_trong_luong:
            file.write(f"{trong_luong:.2f}\n") 
    with open('CANCELED.OUT', 'w') as file:
        file.write(" ".join(huy_chuyen)) 
xu_ly_hanh_khach()