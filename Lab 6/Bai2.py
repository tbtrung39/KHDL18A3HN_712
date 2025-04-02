#Bai2
n = int(input("Nhập số phần tử của danh sách: ")) 
lst = []
print("Nhập", n, "số tự nhiên:")
for i in range(n): 
    so = int(input()) 
    lst.append(so)
print("Danh sách đã nhập:", lst)
#a.Tìm phần tử lớn thứ hai của danh sách và vị trí của nó
ko_trung_lap_lst = []
for so in lst: 
    if so not in ko_trung_lap_lst: 
        ko_trung_lap_lst.append(so)
if len(ko_trung_lap_lst) < 2: 
    print("Không có phần tử lớn thứ hai!")
else: 
    ko_trung_lap_lst.sort(reverse=True)
    pt_lon_thu_2 = ko_trung_lap_lst[1] 
    vi_tri = []
    for i in range(len(lst)): 
        if lst[i] == pt_lon_thu_2: 
            vi_tri.append(i)
    print("Phần tử lớn thứ hai là", pt_lon_thu_2)
    print("Vị trí của phần tử lớn thứ hai là:", vi_tri)
#b.Tính số lượng các số dương liên tiếp nhiều nhất
so_duong_lon_nhat = 0 
so_duong = 0 
for so in lst: 
    if so > 0: 
        so_duong += 1 
    so_duong_lon_nhat = max(so_duong_lon_nhat, so_duong) 
    else: 
        so_duong = 0 
print("Số lượng số dương liên tiếp nhiều nhất:", so_duong_lon_nhat)
#c.Tính số lượng các số dương liên tiếp có tổng lớn nhất
tong_lon_nhat = 0 
tong_tam_thoi = 0 
for so in lst: 
    if so > 0: 
        tong_tam_thoi += so 
    tong_lon_nhat = max(tong_lon_nhat, tong_tam_thoi) 
    else: 
        tong_tam_thoi = 0 
print("Tổng lớn nhất của dãy số dương liên tiếp là:", tong_lon_nhat)