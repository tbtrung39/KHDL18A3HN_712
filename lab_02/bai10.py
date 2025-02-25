gio_bat_dau = int(input("Nhập giờ bắt đầu (5-22): "))
gio_ket_thuc = int(input("Nhập giờ kết thúc (5-22): "))

if 5 <= gio_bat_dau <= 22 and 5 <= gio_ket_thuc <= 22 and gio_bat_dau <= gio_ket_thuc:
    so_gio = gio_ket_thuc - gio_bat_dau
    if so_gio <= 3:
        tien_thue = so_gio * 100000
    else:
        tien_thue = 3 * 100000 + (so_gio - 3) * 75000  
    if 11 <= gio_bat_dau <= 15:
        tien_thue *= 0.9  
    print(f"Số tiền phải trả là: {tien_thue:} đồng")
else:
    print("Giờ nhập vào không hợp lệ. Vui lòng nhập lại.")