import random
so_phan_tu_A = int(input("Nhập số phần tử của tập hợp A: "))
danh_sach_ky_tu = input("Nhập các ký tự tùy ý, không có khoảng trắng: ")
danh_sach_so_nguyen = list(range(1, 100))
danh_sach_so_thuc = [x / 10 for x in range(1, 100)]
danh_sach_tong = danh_sach_so_nguyen + danh_sach_so_thuc + list(danh_sach_ky_tu)
tap_hop_A = set(random.sample(danh_sach_tong, k=min(so_phan_tu_A, len(danh_sach_tong))))
so_nguyen = sum(1 for x in tap_hop_A if type(x) == int)
so_thuc = sum(1 for x in tap_hop_A if type(x) == float)
so_ky_tu = sum(1 for x in tap_hop_A if type(x) == str)
print("Tập hợp A:", tap_hop_A)
print(f"Số lượng số nguyên: {so_nguyen}")
print(f"Số lượng số thực: {so_thuc}")
print(f"Số lượng ký tự: {so_ky_tu}")