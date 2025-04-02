# 1.
lst = [2,-4,1,9,-3,6,3,-2,6,8]
tong = sum(lst)
print('tổng các phần tử trong lst là:', tong)
# 2.
so_duong = [x for x in lst if x > 0]
so_luong_duong = len(so_duong)
tong_duong = sum(so_duong)
print('số lượng số dương:', so_luong_duong)
print('tổng các số dương:', tong_duong)
# 3.
vi_tri_am_dau = next((i for i, x in enumerate(lst) if x < 0), -1)
print('vị trí phần tử âm đầu tiên:', vi_tri_am_dau)
# 4.
vi_tri_duong_cuoi = next((i for i in range(len(lst)-1, -1, -1) if lst[i] > 0), -1)
print('vị trí phần tử dương cuối cùng:', vi_tri_duong_cuoi)
# 5.
gia_tri_lon_nhat = max(lst)
vi_tri_lon_nhat_cuoi = len(lst) - 1 - lst[::-1].index(gia_tri_lon_nhat)
print('phần tử lớn nhất:', gia_tri_lon_nhat)
print('vị trí phần tử nhất nhất cuối cùng:', vi_tri_lon_nhat_cuoi)
