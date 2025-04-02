
danhsach = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
tong = sum(danhsach)
print(f"Tổng các phần tử trong danh sách: {tong}")
print('1. Đếm số lượng số dương và tính tổng các số dương:\n')
so_duong = [x for x in danhsach if x > 0]
so_luong_duong = len(so_duong)
tong_duong = sum(so_duong)
print(f"Số lượng số dương: {so_luong_duong}, Tổng các số dương: {tong_duong}")
print('2.Tìm vị trí của phần tử âm đầu tiên\n')
vi_tri_am_dau = -1
for i in range(len(danhsach)):
    if danhsach[i] < 0:
        vi_tri_am_dau = i
        break
print(f"Vị trí của phần tử âm đầu tiên: {vi_tri_am_dau}")
print('3.Tìm vị trí của phần tử dương cuối cùng\n')
vi_tri_duong_cuoi = -1
for i in range(len(danhsach) - 1, -1, -1):
    if danhsach[i] > 0:
        vi_tri_duong_cuoi = i
        break
print(f"Vị trí của phần tử dương cuối cùng: {vi_tri_duong_cuoi}")
print('4.Tìm phần tử lớn nhất và vị trí xuất hiện cuối cùng\n')
max_gia_tri = danhsach[0]
vi_tri_max_cuoi = 0
for i in range(len(danhsach)):
    if danhsach[i] > max_gia_tri:
        max_gia_tri = danhsach[i]
        vi_tri_max_cuoi = i
    elif danhsach[i] == max_gia_tri:
        vi_tri_max_cuoi = i
print(f"Phần tử lớn nhất: {max_gia_tri}, Vị trí xuất hiện cuối cùng: {vi_tri_max_cuoi}")
