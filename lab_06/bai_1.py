a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]

#1
tong = sum(a)
print("Tong cac phan tu:", tong)

#2
so_luong_duong = 0
tong_so_duong = 0
for x in a:
    if x > 0:
        so_luong_duong += 1
        tong_so_duong += x
print("So luong so hang duong:", so_luong_duong)
print("Tong cac so hang duong:", tong_so_duong)

#3
vi_tri_am_dau = -1
for i in range(len(a)):
    if a[i] < 0:
        vi_tri_am_dau = i
        break
print("Vi tri phan tu am dau tien:", vi_tri_am_dau)

#4
vi_tri_duong_cuoi = -1
for i in range(len(a) - 1, -1, -1):
    if a[i] > 0:
        vi_tri_duong_cuoi = i
        break
print("Vi tri phan tu cuoi cung:", vi_tri_duong_cuoi)

#5
phan_tu_lon_nhat = max(a)
vi_tri_max_cuoi = -1
for i in range(len(a) - 1, -1, -1):
    if a[i] == phan_tu_lon_nhat:
        vi_tri_max_cuoi = i
        break
print("Phan tu lon nhat:", phan_tu_lon_nhat)
print("Vi tri phan tu lon nhat cuoi cung:", vi_tri_max_cuoi)