gio_bat_dau = int(input("Nhập giờ bắt đầu thuê sân: "))
gio_ket_thuc = int(input("Nhập giờ kết thúc thuê sân: "))

tong_gio = gio_ket_thuc - gio_bat_dau

if tong_gio <= 3:
    tien_thue = tong_gio * 100000
    print(tong_gio, "x 100000 =", tien_thue, "đồng")
else:
    tien_gio_dau = 3 * 100000
    tien_gio_sau = (tong_gio - 3) * (100000 * 0.75)
    tien_thue = tien_gio_dau + tien_gio_sau
    print("3 x 100000 =", tien_gio_dau, "đồng")
    print(tong_gio - 3, "x 75000 =", tien_gio_sau, "đồng")

if gio_bat_dau < 15 and gio_ket_thuc > 11:
    tien_giam = tien_thue * 0.1
    tien_thue *= 0.9
    print("Giảm 10% do thuê từ 11h - 15h:", tien_giam, "đồng")

print("Tổng số tiền phải trả:", tien_thue, "đồng")