import random
n = int(input("Nhap so luong phan tu: "))
A = set()
while len(A) < n:
    A.add(round(random.uniform(0, 100), 2)) 

print("Tap hop A:", A)
print("Phan tu nho nhat:", min(A))
print("Phan tu lon nhat:", max(A))
print("Tong cac phan tu:", sum(A))