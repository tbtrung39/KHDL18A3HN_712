# bai 1
# Khởi tạo danh sách a
a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
tong = 0
for so in a:
    tong = tong + so
so_luong_duong = 0
tong_duong = 0
for so in a:
    if so > 0:
        so_luong_duong = so_luong_duong + 1
        tong_duong = tong_duong + so
vi_tri_am_dau_tien = -1
for i in range(len(a)):
    if a[i] < 0:
        vi_tri_am_dau_tien = i
        break
vi_tri_duong_cuoi_cung = -1
for i in range(len(a)-1, -1, -1):
    if a[i] > 0:
        vi_tri_duong_cuoi_cung = i
        break
gia_tri_lon_nhat = a[0]
vi_tri_lon_nhat_cuoi = 0
for i in range(len(a)):
    if a[i] >= gia_tri_lon_nhat:
        gia_tri_lon_nhat = a[i]
        vi_tri_lon_nhat_cuoi = i
print("Tổng các phần tử trong danh sách:", tong)
print("Số lượng số dương trong danh sách:", so_luong_duong)
print("Tổng các số dương trong danh sách:", tong_duong)
print("Vị trí của phần tử âm đầu tiên:", vi_tri_am_dau_tien)
print("Vị trí của phần tử dương cuối cùng:", vi_tri_duong_cuoi_cung)
print("Phần tử lớn nhất trong danh sách:", gia_tri_lon_nhat)
print("Vị trí của phần tử lớn nhất cuối cùng:", vi_tri_lon_nhat_cuoi)
