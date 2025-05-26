danh_sach = []
print("Nhập các số tự nhiên (nhập 0 để kết thúc):")
while True:
    so = int(input())
    if so == 0:
        break
    danh_sach.append(so)

so_duong = [x for x in danh_sach if x > 0]
so_khong_duong = [x for x in danh_sach if x <= 0]
danh_sach = so_duong + so_khong_duong
print("Danh sách sau khi đưa các số dương lên đầu:")
print(danh_sach)
m = int(input("Nhập số m cần chèn: "))
danh_sach.insert(0, m)
danh_sach.append(m)
if len(danh_sach) >= 5:
    danh_sach.insert(4, m)
else:
    print("Danh sách có ít hơn 4 phần tử, không thể chèn vào vị trí thứ 5.")

print("Danh sách sau khi chèn số m vào đầu, cuối và vị trí thứ 5:")
print(danh_sach)