gio_bat_dau = int(input("Nhập giờ bắt đầu : "))
gio_ket_thuc = int(input("Nhập giờ kết thúc : "))
if gio_bat_dau < 5 or gio_bat_dau > 22:
    print(" sai giờ vui lòng nhập lại")
elif gio_ket_thuc < 5 or gio_ket_thuc > 22:
    print("sai giờ vui lòng nhập lại")
elif gio_bat_dau >= gio_ket_thuc:
    print("sai giờ vui lòng nhập lại")
else:
    so_gio_thue = gio_ket_thuc - gio_bat_dau
    gia_3_gio_dau = 100000
    tien_thue_san = 0
    if so_gio_thue <= 3:
        tien_thue = so_gio_thue * gia_3_gio_dau
    else:
        tien_thue = 3 * gia_3_gio_dau  
        so_gio_thue -= 3 
        don_gia_tiep_theo = gia_3_gio_dau 
        tien_thue += so_gio_thue * don_gia_tiep_theo  
#từ 11h-15h giảm giá 10% 
    if gio_bat_dau >= 11 and gio_bat_dau < 15:
        tien_thue *= 0.9  
    print(f"Số tiền bạn phải trả là: {tien_thue:.0f} đồng")

