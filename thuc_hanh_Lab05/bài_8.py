van_ban = input("Nhập đoạn văn: ")
tu_don = input("Nhập từ đơn cần tìm: ")
danh_sach_tu = van_ban.split()
so_lan_xuat_hien = 0
for tu in danh_sach_tu:
    if tu == tu_don:
        so_lan_xuat_hien += 1
print(f"Từ '{tu_don}' xuất hiện {so_lan_xuat_hien} lần trong đoạn văn.")
