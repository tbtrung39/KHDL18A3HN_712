# bai 2
# Nhập số phần tử của danh sách
n = int(input("Nhập số phần tử của danh sách: "))

# Khởi tạo danh sách rỗng
danh_sach = []

# Nhập danh sách từ bàn phím
for i in range(n):
    so = int(input("Nhập phần tử thứ " + str(i + 1) + ": "))
    danh_sach.append(so)

# Tìm phần tử lớn thứ hai và vị trí của nó
lon_nhat = danh_sach[0]
lon_thu_hai = danh_sach[0]
vi_tri_lon_thu_hai = -1

# Tìm phần tử lớn nhất
for i in range(n):
    if danh_sach[i] > lon_nhat:
        lon_nhat = danh_sach[i]

# Tìm phần tử lớn thứ hai (nhỏ hơn phần tử lớn nhất)
for i in range(n):
    if danh_sach[i] < lon_nhat:
        lon_thu_hai = danh_sach[i]
        break  # Tìm được giá trị nhỏ hơn lớn nhất thì dừng

# Tìm lại phần tử lớn thứ hai chính xác nhất
for i in range(n):
    if danh_sach[i] > lon_thu_hai and danh_sach[i] < lon_nhat:
        lon_thu_hai = danh_sach[i]

# Tìm vị trí của phần tử lớn thứ hai xuất hiện đầu tiên
for i in range(n):
    if danh_sach[i] == lon_thu_hai:
        vi_tri_lon_thu_hai = i
        break

# Tính số lượng các số dương liên tiếp nhiều nhất
dem = 0
so_luong_lon_nhat = 0
for i in range(n):
    if danh_sach[i] > 0:
        dem = dem + 1
    else:
        if dem > so_luong_lon_nhat:
            so_luong_lon_nhat = dem
        dem = 0

if dem > so_luong_lon_nhat:
    so_luong_lon_nhat = dem

# Tính số lượng các số dương liên tiếp có tổng lớn nhất
tong_hien_tai = 0
tong_lon_nhat = 0
do_dai_tong_lon_nhat = 0
dem = 0

for i in range(n):
    if danh_sach[i] > 0:
        tong_hien_tai = tong_hien_tai + danh_sach[i]
        dem = dem + 1
    else:
        if tong_hien_tai > tong_lon_nhat:
            tong_lon_nhat = tong_hien_tai
            do_dai_tong_lon_nhat = dem
        tong_hien_tai = 0
        dem = 0
if tong_hien_tai > tong_lon_nhat:
    tong_lon_nhat = tong_hien_tai
    do_dai_tong_lon_nhat = dem
print("Phần tử lớn thứ hai trong danh sách:", lon_thu_hai, "tại vị trí", vi_tri_lon_thu_hai)
print("Số lượng các số dương liên tiếp nhiều nhất:", so_luong_lon_nhat)
print("Số lượng các số dương liên tiếp có tổng lớn nhất:", do_dai_tong_lon_nhat)