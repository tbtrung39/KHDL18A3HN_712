gio_batdau = int(input("Nhập giờ bắt đầu (5-22): "))
gio_ketthuc = int(input("Nhập giờ kết thúc (5-22): "))
luong = 100000
luongthuong = luong * 0.75
if 5 <= gio_batdau <= 22 and 5 <= gio_ketthuc <= 22 and gio_batdau < gio_ketthuc:
    total_price = 3 * luong + (gio_ketthuc - gio_batdau - 3) * luongthuong if gio_ketthuc - gio_batdau > 3 else (gio_ketthuc - gio_batdau) * luong
    if 11 <= gio_batdau < 15:
        total_price *= 0.9
    print(f"Tổng tiền thuê sân: {total_price} đồng")
else:
    print("Giờ không hợp lệ!")
