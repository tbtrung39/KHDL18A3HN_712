danh_sach = []
while True:
    so = int(input("Nhập số tự nhiên (nhập 0 để kết thúc): "))
    if so == 0:
        break
    danh_sach.append(so)

duong = [x for x in danh_sach if x > 0]
am_va_khong = [x for x in danh_sach if x <= 0]
danh_sach_moi = duong + am_va_khong

print("Danh sách sau khi sắp xếp:")
print(danh_sach_moi)
m = int(input("\nNhập số m cần thêm: "))
danh_sach_moi.insert(0, m)
danh_sach_moi.append(m)

if len(danh_sach_moi) >= 5:
    danh_sach_moi.insert(4, m)
print("\nDanh sách sau khi chèn m:")
print(danh_sach_moi)