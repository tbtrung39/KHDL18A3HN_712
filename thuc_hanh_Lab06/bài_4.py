danh_sach = []
so = int(input("Nhập một số tự nhiên (nhập 0 để kết thúc): "))
while so != 0:
    danh_sach.append(so)
    so = int(input("Nhập một số tự nhiên (nhập 0 để kết thúc): "))
print("Danh sách vừa nhập:", danh_sach)
danh_sach_chen = [1, 2, 3]
danh_sach = danh_sach_chen + danh_sach
danh_sach = danh_sach + danh_sach_chen
if len(danh_sach) >= 5:
    danh_sach = danh_sach[:4] + danh_sach_chen + danh_sach[4:]
print("Danh sách sau khi chèn:", danh_sach)
k = int(input("Nhập vị trí k cần xóa (bắt đầu từ 1): "))
if 1 <= k <= len(danh_sach):
    del danh_sach[k - 1]  
    print("Danh sách sau khi xóa phần tử thứ", k, ":", danh_sach)
else:
    print("Vị trí k không hợp lệ.")
danh_sach_tang_dan = sorted(danh_sach)
print("Danh sách tăng dần:", danh_sach_tang_dan)
danh_sach_giam_dan = sorted(danh_sach, reverse=True)
print("Danh sách giảm dần:", danh_sach_giam_dan)

