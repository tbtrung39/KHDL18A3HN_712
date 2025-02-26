print("Nhập giờ bắt đầu:", end=" ")
gio_bd = int(input())
print("Nhập giờ kết thúc:", end=" ")
gio_kt = int(input())
if 5 <= gio_bd <= gio_kt <= 22:
    # Tính tổng số giờ thuê
    so_gio = gio_kt - gio_bd
    gia_3h_dau = 100000  # Giá 3 giờ đầu tiên
    gia_giam = gia_3h_dau * 0.75  # Giá từ giờ thứ 4 trở đi
    if so_gio <= 3:
        tien_thue = so_gio * gia_3h_dau
    else:
        tien_thue = 3 * gia_3h_dau + (so_gio - 3) * gia_giam
    if gio_bd < 15 and gio_kt > 11:
        tien_thue *= 0.9  # Giảm 10%
    print("Số tiền khách phải trả là:", int(tien_thue), "đồng")
else:
    print("Giờ nhập không hợp lệ! Vui lòng nhập trong khoảng 5 đến 22 giờ.")
