gio_bat_dau = int(input("Nhập giờ bắt đầu thuê sân (5 -> 22): "))
gio_ket_thuc = int(input("Nhập giờ kết thúc thuê sân (5 -> 22): "))

if 5 <= gio_bat_dau <= gio_ket_thuc <= 22:
    so_gio = gio_ket_thuc - gio_bat_dau
    gia_3_gio_dau = 100000
    gia_sau_3_gio_dau = gia_3_gio_dau * 0.75
    
    if so_gio <= 3:
        tong_tien = so_gio * gia_3_gio_dau
    else:
        tong_tien = 3 * gia_3_gio_dau + (so_gio - 3) * gia_sau_3_gio_dau
    
    if gio_bat_dau < 15 and gio_ket_thuc > 11:
        tong_tien *= 0.9
    
    print("Số tiền khách phải trả là:", int(tong_tien), "đồng")
else:
    print("Giờ nhập không hợp lệ! Vui lòng nhập lại.")