#Bai3
import random
n = int(input("Nhập số phần tử n: "))
A = set()
for i in range(n):
    A.add(float(random.randint(0, 100)))
pt_nho_nhat = min(A)
pt_lon_nhat = max(A)
tong_pt = sum(A)
print("Tập hợp A:", A)
print("Phần tử nhỏ nhất của tập hợp A:", pt_nho_nhat)
print("Phần tử lớn nhất của tập hợp A:", pt_lon_nhat)
print("Tổng các phần tử của tập hợp A:", tong_pt)