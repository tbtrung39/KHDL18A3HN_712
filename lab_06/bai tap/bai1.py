
a = [-12, -4, 1, 9, -3, 6, 3, -2, 6, 81]


tong = sum(a)
print("Tổng các phần tử của danh sách:", tong)


so_luong_duong = 0
tong_duong = 0
for x in a:
    if x > 0:
        so_luong_duong += 1
        tong_duong += x

print("Số lượng số hạng dương:", so_luong_duong)
print("Tổng các số hạng dương:", tong_duong)


vi_tri_am_dau_tien = -1
for i in range(len(a)):
    if a[i] < 0:
        vi_tri_am_dau_tien = i
        break
print("Vị trí phần tử âm đầu tiên:", vi_tri_am_dau_tien)


vi_tri_duong_cuoi_cung = -1
for i in range(len(a) - 1, -1, -1):
    if a[i] > 0:
        vi_tri_duong_cuoi_cung = i
        break
print("Vị trí phần tử dương cuối cùng:", vi_tri_duong_cuoi_cung)


max_value = max(a)
vi_tri_max_cuoi = -1
for i in range(len(a) - 1, -1, -1):
    if a[i] == max_value:
        vi_tri_max_cuoi = i
        break
print("Phần tử lớn nhất:", max_value)
print("Vị trí cuối cùng của phần tử lớn nhất:", vi_tri_max_cuoi)
