# Nhập danh sách số tự nhiên cho đến khi gặp số 0
danh_sach = []
while True:
    num = int(input("Nhập số (0 để dừng): "))
    if num == 0:
        break
    danh_sach.append(num)

# Chuyển số dương lên đầu danh sách
danh_sach.sort(key=lambda x: x <= 0)

# In danh sách sau khi chuyển số dương lên đầu
print("Danh sách sau khi chuyển số dương lên đầu:", danh_sach)

# Nhập số m
m = int(input("Nhập số m: "))
# Chèn số m vào đầu danh sách, cuối danh sách và vị trí thứ 5
danh_sach.insert(0, m)  # Chèn vào đầu danh sách
danh_sach.append(m)  # Chèn vào cuối danh sách
if len(danh_sach) >= 5:
    danh_sach.insert(4, m)  # Chèn vào vị trí thứ 5
# In danh sách sau khi chèn số m
print("Danh sách sau khi chèn số m:", danh_sach)