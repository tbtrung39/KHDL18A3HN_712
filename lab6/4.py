# bai 4
danh_sach = []
while True:
    num = int(input("Nhập số (0 để dừng): "))
    if num == 0:
        break
    danh_sach.append(num)

# Chèn danh sách [1, 2, 3] vào vị trí đầu, cuối và thứ 5 của danh sách
danh_sach = [1, 2, 3] + danh_sach 
danh_sach.append(1)  
if len(danh_sach) >= 5:
    danh_sach.insert(4, 1)  # Chèn vào vị trí thứ 5 (chỉ số 4 trong Python)

# In danh sách sau khi chèn
print("Danh sách sau khi chèn [1, 2, 3]:", danh_sach)
# Xóa phần tử thứ k trong danh sách
k = int(input("Nhập vị trí k để xóa phần tử thứ k: "))
if 0 <= k < len(danh_sach):
    # Tạo một danh sách mới mà không có phần tử thứ k
    danh_sach = danh_sach[:k] + danh_sach[k+1:]
else:
    print("Vị trí không hợp lệ!")
# In danh sách sau khi xóa
print("Danh sách sau khi xóa phần tử thứ k:", danh_sach)
# Sắp xếp danh sách theo thứ tự tăng dần và giảm dần
danh_sach.sort()  # Sắp xếp tăng dần
print("Danh sách sau khi sắp xếp tăng dần:", danh_sach)
danh_sach.sort(reverse=True)  # Sắp xếp giảm dần
print("Danh sách sau khi sắp xếp giảm dần:", danh_sach)