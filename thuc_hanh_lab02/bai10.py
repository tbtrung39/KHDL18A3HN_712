gio = int(input("Nhập số giờ thuê sân: "))

if gio <= 3:
    tien_thue = gio * 100000
else:
    tien_thue = 3 * 100000 + (gio - 3) * 150000

print(f"Tiền thuê sân là: {tien_thue} đồng.")
