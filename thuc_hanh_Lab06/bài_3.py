print('1.\n')
danh_sach = []
so = int(input("Nhập một số tự nhiên (nhập 0 để kết thúc): "))
while so != 0:
    danh_sach.append(so)
    so = int(input("Nhập một số tự nhiên (nhập 0 để kết thúc): "))
danh_sach_duong = []
danh_sach_con_lai = []
for phan_tu in danh_sach:
    if phan_tu > 0:
        danh_sach_duong.append(phan_tu)
    else:
        danh_sach_con_lai.append(phan_tu)
danh_sach_moi = danh_sach_duong + danh_sach_con_lai
print("Danh sách sau khi chuyển các phần tử dương lên đầu:")
print(danh_sach_moi)
print('2.\n')
m = int(input("Nhập số m cần chèn: "))
danh_sach_moi.insert(0, m)  
danh_sach_moi.append(m)  
if len(danh_sach_moi) >= 5:
    danh_sach_moi.insert(4, m)  
print("Danh sách sau khi chèn số m:")
print(danh_sach_moi)