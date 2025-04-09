n = int(input("Nhập số lượng phần tử: "))
danh_sach_ten = [input(f"Nhập tên thứ {i+1}: ") for i in range(n)]
danh_sach_gia_tri = [input(f"Nhập giá trị thứ {i+1}: ") for i in range(n)]
tu_dien = {danh_sach_ten[i]: danh_sach_gia_tri[i] for i in range(n)}
print("\nNội dung của từ điển:")
for key, value in tu_dien.items():
    print(f'{key}: {value}')
