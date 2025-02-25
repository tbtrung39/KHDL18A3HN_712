gio_bat_dau = int(input("Nhập giờ bắt đầu (5-22): "))
gio_ket_thuc = int(input("Nhập giờ kết thúc (5-22): "))

if gio_bat_dau < 5 or gio_ket_thuc > 22 or gio_bat_dau >= gio_ket_thuc:
    print("Giờ không hợp lệ!")
else:
    so_gio = gio_ket_thuc - gio_bat_dau
    gia_goc = 100000
    if so_gio <= 3:
        tien = so_gio * gia_goc
    else:
        tien = 3 * gia_goc + (so_gio - 3) * (gia_goc * 0.75)

    if 11 <= gio_bat_dau <= 15 or 11 <= gio_ket_thuc <= 15:
        tien *= 0.9 

    print("Số tiền cần trả:", int(tien), "đồng")
