import random
a = set()
n = float(input("Nhap so phan tu: "))
while len(a) < n:
    a.add(round(random.uniform(0, 100), 3))
    
print("a = ", a)
print("Phan tu nho nhat: ", min(a))
print("Phan tu lon nhat: ", max(a))
print("Tong cac phan tu: ", sum(a))