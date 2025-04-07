import random
A = set()
n = float(input("Nhap so phan tu: "))
while len(A) < n:
    A.add(round(random.uniform(0, 100), 3))
    
print("A = ", A)
print("Phan tu nho nhat: ", min(A))
print("Phan tu lon nhat: ", max(A))
print("Tong cac phan tu: ", sum(A))