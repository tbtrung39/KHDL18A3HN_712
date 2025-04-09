import random
n = int(input("Nhập số lượng phần tử: "))
A = [round(random.uniform(0, 100), 2) for _ in range(n)]
print("Danh sách A:", A)
print("Giá trị nhỏ nhất:", min(A))
print("Giá trị lớn nhất:", max(A))
print("Tổng các phần tử:", sum(A))
