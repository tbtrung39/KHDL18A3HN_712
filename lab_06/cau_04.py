danh_sach = []
while True:
    so = int(input("Nhập số (0 để dừng): "))
    if so == 0:
        break
    danh_sach.append(so)
print("Danh sách ban đầu:", danh_sach)
chen = [1, 2, 3]
danh_sach = chen + danh_sach
if len(danh_sach) >= 5:
    danh_sach[5:5] = chen
else:
    print("Danh sách chưa đủ 5 phần tử, không thể chèn vào vị trí thứ 5.")
danh_sach += chen
print("Danh sách sau khi chèn:", danh_sach)

m = int(input("Nhập vị trí cần xóa (tính từ 0): "))
if 0 <= m < len(danh_sach):
    del danh_sach[m]
    print(f"Danh sách sau khi xóa phần tử ở vị trí {m}:", danh_sach)
else:
    print("Vị trí không hợp lệ, không thể xóa.")

danh_sach_tang = sorted(danh_sach)
danh_sach_giam = sorted(danh_sach, reverse=True)
print("Danh sách sắp xếp tăng dần:", danh_sach_tang)
print("Danh sách sắp xếp giảm dần:", danh_sach_giam)
