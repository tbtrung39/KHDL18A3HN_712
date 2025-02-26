gio_bat_dau = int(input("Nhập giờ bắt đầu thuê sân tập bóng đá là: "))
gio_ket_thuc = int(input("Nhập giờ kết thúc thuê sân tập bóng đá là: "))
if 5 <= gio_bat_dau <= gio_ket_thuc <= 22:
    tong_so_gio = gio_ket_thuc - gio_bat_dau
    tien_thue_san = 0
    tien_thue_san = int(tien_thue_san)
    if tong_so_gio <= 3:
        tien_thue_san = tong_so_gio * 100000
    else:
        tien_thue_san = 3 * 100000 + (tong_so_gio - 3) * 75000
    if gio_bat_dau < 15 <= gio_ket_thuc or gio_bat_dau <= 11 < gio_ket_thuc:
        tien_thue_san *= 0.9
    print("Số tiền khách thuê sân phải trả là:",tien_thue_san, "đồng")
else:
    print("Bạn đã nhập sai giờ.")        