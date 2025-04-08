# bai 19
# a
nhan_vien = {}

# b
n = int(input("Nhập số lượng nhân viên: "))

for i in range(n):
    print(f"\nNhập thông tin cho nhân viên thứ {i+1}:")
    ma = input(" - Mã nhân viên (4 chữ số): ")
    ho_ten = input(" - Họ tên (tối đa 20 ký tự): ")
    nam_sinh = int(input(" - Năm sinh: "))
    luong = int(input(" - Lương: "))
    
    nhan_vien[ma] = {"ho_ten": ho_ten, "nam_sinh": nam_sinh, "luong": luong}

#c
x = input("\nNhập mã nhân viên cần tìm: ")
if x in nhan_vien:
    print(f" - Tìm thấy: {nhan_vien[x]}")
else:
    print(" - Không tìm thấy mã nhân viên.")

# d
y = input("\nNhập mã nhân viên cần tăng lương: ")
if y in nhan_vien:
    nhan_vien[y]["luong"] += 1000000
    print(" - Đã tăng lương.")
else:
    print(" - Không tìm thấy mã nhân viên để tăng lương.")

# e. 
z = input("\nNhập mã nhân viên cần xóa: ")
if z in nhan_vien:
    del nhan_vien[z]
    print(" - Đã xóa nhân viên.")
else:
    print(" - Không tìm thấy mã nhân viên để xóa.")
print("\nDanh sách nhân viên sau khi sắp xếp theo năm sinh giảm dần:")
sorted_nv = sorted(nhan_vien.items(), key=lambda item: item[1]["nam_sinh"], reverse=True)
for ma, info in sorted_nv:
    print(f"{ma}: {info['ho_ten']} - {info['nam_sinh']} - {info['luong']}")
