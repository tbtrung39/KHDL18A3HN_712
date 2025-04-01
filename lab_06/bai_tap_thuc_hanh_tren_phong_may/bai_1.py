a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]

#1
tong = sum(a)
print("Tổng các phần tử:", tong)

#2
so_duong = [x for x in a if x > 0]
so_luong_duong = len(so_duong)
tong_duong = sum(so_duong)
print("Số lượng số dương:", so_luong_duong)
print("Tổng các số dương:", tong_duong)

#3
vi_tri_am_dau = next((i for i, x in enumerate(a) if x < 0), -1)
print("Vị trí phần tử âm đầu tiên:", vi_tri_am_dau)

#4
vi_tri_duong_cuoi = next((i for i in range(len(a) - 1, -1, -1) if a[i] > 0), -1)
print("Vị trí phần tử dương cuối cùng:", vi_tri_duong_cuoi)

#5
phan_tu_lon_nhat = max(a)
vi_tri_phan_tu_lon_nhat_cuoi = len(a) - 1 - a[::-1].index(phan_tu_lon_nhat)
print("Phần tử lớn nhất:", phan_tu_lon_nhat)
print("Vị trí phần tử lớn nhất cuối cùng:", vi_tri_phan_tu_lon_nhat_cuoi)