# Nhập vào số phần tử n
n = int(input("Nhập số phần tử của danh sách A: "))

# Nhập danh sách A từ bàn phím
A = [int(input(f"Nhập phần tử thứ {i+1}: ")) for i in range(n)]

# a. Tạo danh sách B chứa các phần tử chia hết cho 3 nhưng không chia hết cho 5
B = [x for x in A if x % 3 == 0 and x % 5 != 0]

# b. Tạo danh sách C với các phần tử là bình phương của danh sách A
C = [x**2 for x in A]

# c. Tạo danh sách D gồm các phần tử ngẫu nhiên từ A mà chia hết cho 3 (không dùng thư viện random)
D = [A[i] for i in range(len(A)) if A[i] % 3 == 0 and i % 2 == 0]  

# In kết quả
print("Danh sách A:", A)
print("Danh sách B (chia hết cho 3 nhưng không chia hết cho 5):", B)
print("Danh sách C (bình phương của A):", C)
print("Danh sách D (lấy ngẫu nhiên từ A mà chia hết cho 3):", D)