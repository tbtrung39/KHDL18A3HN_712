so_phan_tu = int(input("Nhập số phần tử của danh sách: "))
danh_sach = list(map(int, input("Nhập danh sách số: ").split()))
if so_phan_tu < 2:
    print("Không có phần tử lớn thứ hai")
else:
    lon_nhat = danh_sach[0]
    lon_nhi = danh_sach[0]
    vi_tri_lon_nhi = -1
    vi_tri_lon_nhat = 0 
    for i in range(1, so_phan_tu):
        if danh_sach[i] > lon_nhat:
            lon_nhi = lon_nhat 
            vi_tri_lon_nhi = vi_tri_lon_nhat 
            lon_nhat = danh_sach[i]
            vi_tri_lon_nhat = i 
        elif danh_sach[i] > lon_nhi and danh_sach[i] != lon_nhat:
            lon_nhi = danh_sach[i]
            vi_tri_lon_nhi = i
    if lon_nhi == lon_nhat:
        print("Không có phần tử lớn thứ hai")
    else:
        print(f"Phần tử lớn thứ hai: {lon_nhi}, vị trí: {vi_tri_lon_nhi}")

dem_max = 0
dem_hien_tai = 0
for so in danh_sach:
    if so > 0:
        dem_hien_tai += 1
        if dem_hien_tai > dem_max:
            dem_max = dem_hien_tai
    else:
        dem_hien_tai = 0
print(f"Số lượng số dương liên tiếp nhiều nhất: {dem_max}")

tong_max = danh_sach[0] if danh_sach else 0
tong_hien_tai = 0
so_phan_tu_max = 0
so_phan_tu_hien_tai = 0
for so in danh_sach:
    if so > 0:
        tong_hien_tai += so
        so_phan_tu_hien_tai += 1
        if tong_hien_tai > tong_max:
            tong_max = tong_hien_tai
            so_phan_tu_max = so_phan_tu_hien_tai
    else:
        tong_hien_tai = 0
        so_phan_tu_hien_tai = 0
print(f"Số lượng số dương liên tiếp có tổng lớn nhất: {so_phan_tu_max}")
