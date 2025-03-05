gio_bat_dau = float(input('Nhập giờ bắt đầu (5 <= và <= 22): '))
gio_ket_thuc = float(input('Nhập giờ kết thúc ( <= 22): '))
if gio_bat_dau < 5 or gio_bat_dau > 22 or gio_ket_thuc < gio_bat_dau or gio_ket_thuc > 22:
    print('Giờ không hợp lệ. Vui lòng nhập lại!')
else:
    so_gio_thue = gio_ket_thuc - gio_bat_dau
    gia_3_gio_dau = 100000
    gia_sau_3_gio = gia_3_gio_dau * 0.75
    if so_gio_thue <= 3:
        tien_thue = so_gio_thue * gia_3_gio_dau
    else:
        tien_thue = 3 * gia_3_gio_dau + (so_gio_thue - 3) * gia_sau_3_gio
    if gio_bat_dau < 15 and gio_ket_thuc > 11:
        tien_thue *= 0.9
    print(f'Số tiền khách thuê sân phải trả là: {tien_thue:,.0f} đ')