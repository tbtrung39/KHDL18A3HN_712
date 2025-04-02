import random

n = int(input("Nhap so phan tu cua danh sach A: "))
A = [int(input(f"Nhap phan tu thu {i+1}: ")) for i in range(n)]

# a)
B = [x for x in A if x%3 == 0 and x%5!= 0]
print("Danh sach B:", B)

# b)
C = [x**2 for x in A]
print("Danh sach C:", C)

# c) 
D = random.sample([x for x in A if x%3 == 0], k = min(len([x for x in A if x%3 == 0]), n))
print("Danh sach D:", D)