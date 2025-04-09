import random
n = int(input("Nhập số lượng phần tử làlà: "))
A = set()
while len(A) < n:
    A.add(round(random.uniform(0, 100), 2))  
print("Tập hợp A:", A)
print("Phần tử nhỏ nhất là:", min(A))
print("Phần tử lớn nhất là:", max(A))
print("Tổng các phần tử là:", sum(A))