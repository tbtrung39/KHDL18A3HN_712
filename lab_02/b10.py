# bài 10
gio_bat_dau = int(input("Nhập giờ bắt đầu thuê sân (5-22): "))
gio_ket_thuc = int(input("Nhập giờ kết thúc thuê sân (5-22): "))
if gio_bat_dau < 5 or gio_ket_thuc > 22 or gio_bat_dau >= gio_ket_thuc:
    print("Thời gian thuê không hợp lệ!")
else:
    tong_gio = gio_ket_thuc - gio_bat_dau
    gia_3h_dau = min(tong_gio, 3) * 100000
    gia_sau_3h = max(0, tong_gio - 3) * (100000 * 0.75)
    tong_tien = gia_3h_dau + gia_sau_3h
    if 11 <= gio_bat_dau < 15 or 11 < gio_ket_thuc <= 15:
        tong_tien *= 0.9  # Giảm 10%
    print("Số tiền phải trả là:", int(tong_tien), "đồng")
