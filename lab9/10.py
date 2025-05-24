def calculate_X(n):
    # Khởi tạo danh sách để lưu trữ các giá trị X
    X = [-1]  # X[0] = -1

    # Tính các giá trị X từ 1 đến n
    for i in range(1, n + 1):
        current_X = 0
        for j in range(i):
            current_X += (i - j) ** 2 * X[j]
        X.append(current_X)

    return X

# Nhập giá trị n
n = int(input("Nhập giá trị n: "))
result = calculate_X(n)

# In ra kết quả
for i in range(n + 1):
    print(f"X[{i}] = {result[i]}")