danh_sach = list(map(int, input("Nhập danh sách số nguyên: ").split()))
so_lon_nhat = danh_sach[0]
for so in danh_sach:
    if so > so_lon_nhat:
        so_lon_nhat = so
print('1. Tìm số lớn thứ hai,vị trí \n')
so_lon_thu_hai = danh_sach[0]
co_so_khac = False  # Kiểm tra có số khác số lớn nhất không
for so in danh_sach:
    if so != so_lon_nhat:
        so_lon_thu_hai = so
        co_so_khac = True
        break
if co_so_khac:
    for so in danh_sach:
        if so != so_lon_nhat and so > so_lon_thu_hai:
            so_lon_thu_hai = so
    vi_tri = []
    for i in range(len(danh_sach)):
        if danh_sach[i] == so_lon_thu_hai:
            vi_tri.append(i)
    print("Phần tử lớn thứ hai là:", so_lon_thu_hai)
    print("Vị trí của nó trong danh sách là:", vi_tri)
else:
    print("Không có phần tử lớn thứ hai")
print('2.Tìm số lượng số dương liên tiếp nhiều nhất\n')
so_luong_lon_nhat = 0  
dem = 0  
for so in danh_sach:
    if so > 0:
        dem = dem + 1
        if dem > so_luong_lon_nhat:
            so_luong_lon_nhat = dem
    else:
        dem = 0 
print("Số lượng số dương liên tiếp nhiều nhất là:", so_luong_lon_nhat)
print('3.\n')
tong_lon_nhat = 0 
so_luong_tong_lon_nhat = 0 
tong_hien_tai = 0  
dem = 0  
for so in danh_sach:
    if so > 0:
        tong_hien_tai = tong_hien_tai + so
        dem = dem + 1
        if tong_hien_tai > tong_lon_nhat:
            tong_lon_nhat = tong_hien_tai
            so_luong_tong_lon_nhat = dem
    else:
        tong_hien_tai = 0 
        dem = 0
print("Số lượng số dương liên tiếp có tổng lớn nhất là:", so_luong_tong_lon_nhat)


