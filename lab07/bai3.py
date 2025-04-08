import random

n = int(input("Nhập số lượng phần tử n: "))
A = {round(random.uniform(0, 100), 2) for _ in range(n)}

print("Tập hợp A:", A)
print("Phần tử nhỏ nhất:", min(A))
print("Phần tử lớn nhất:", max(A))
print("Tổng các phần tử:", round(sum(A), 2))
