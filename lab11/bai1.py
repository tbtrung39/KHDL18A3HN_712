# Đọc file dayso.dat
with open('dayso.dat', 'r') as file:
    # Đọc tất cả các dòng và chuyển thành danh sách các số
    numbers = []
    for line in file:
        # Tách các số trong mỗi dòng và thêm vào danh sách
        numbers.extend([int(num) for num in line.split()])

# Tính tổng các số lẻ
tong_le = sum(num for num in numbers if num % 2 == 1)

# In kết quả
print(f"Tổng các số lẻ trong dãy: {tong_le}")