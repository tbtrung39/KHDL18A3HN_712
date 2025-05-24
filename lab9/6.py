import random

# Nhập số tự nhiên n từ bàn phím
n = int(input("Nhập số tự nhiên n: "))

# Tạo danh sách A chứa các số từ 1 đến n
A = list(range(1, n + 1))

# Tạo danh sách result để lưu hoán vị ngẫu nhiên
result = []

# Lặp cho đến khi danh sách A rỗng
while A:
    # Lấy một phần tử ngẫu nhiên từ A
    index = random.randint(0, len(A) - 1)  # Chọn chỉ số ngẫu nhiên
    result.append(A[index])  # Thêm phần tử vào result
    A.pop(index)  # Xóa phần tử khỏi danh sách A

# In ra kết quả
print("Hoán vị ngẫu nhiên của các số từ 1 đến", n, "là:", result)