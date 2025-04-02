import random
n = int(input("Nhập số lượng phần tử của danh sách A: "))
A = []
for i in range(n):
    so = int(input(f"Nhập phần tử thứ {i + 1}: "))
    A.append(so)
print("Danh sách A:", A)
print('a. Tạo danh sách B chứa các phần tử chia hết cho 3 nhưng không chia hết cho 5:\n')
B = [so for so in A if so % 3 == 0 and so % 5 != 0]
print("Danh sách B:", B)
print('b. Tạo danh sách C với các phần tử là bình phương của danh sách A:\n')
C = [so ** 2 for so in A]
print("Danh sách C:",C)
print('c. Tạo danh sách D gồm các phần tử lấy ngẫu nhiên từ danh sách A mà chia hết cho 3:\n')
D = [random.choice(A) for _ in range(len(A)) if random.choice(A) % 3 == 0]
print("Danh sách D:", D)