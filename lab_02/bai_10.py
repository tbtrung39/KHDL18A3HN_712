gio_bat_dau = int(input("Nhập giờ bắt đầu (từ 5 đến 22): "))
gio_ket_thuc = int(input("Nhập giờ kết thúc (từ 5 đến 22): "))

if 5 <= gio_bat_dau <= gio_ket_thuc <= 22:
    so_gio_thue = gio_ket_thuc - gio_bat_dau
    if so_gio_thue <= 3:
        tong_tien = so_gio_thue * 100000
    else: 
        tong_tien = 3 * 100000
        so_gio_tiep_theo = so_gio_thue - 3
        tong_tien += so_gio_tiep_theo * (100000 * 0.75)  # Giảm 25%

    # Kiểm tra giảm giá 10% nếu thuê trong khoảng từ 11 giờ đến 15 giờ
    if gio_bat_dau >= 11 and gio_ket_thuc <= 15:
        tong_tien *= 0.9  # Giảm 10%

    print("Số tiền khách thuê sân tập phải trả là:", tong_tien, "đồng")
else:
    print("Giờ không hợp lệ, vui lòng nhập lại.")