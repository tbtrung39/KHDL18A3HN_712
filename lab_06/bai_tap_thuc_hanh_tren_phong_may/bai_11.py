import random
n = int(input("Nhập số phần tử của danh sách: "))
A = [int(input(f"Nhập phần tử thứ {i+1}: ")) for i in range(n)]
#a)
B = [x for x in A if x % 3 == 0 and x % 5 != 0]
print("Danh sách B:", B)

# b)
C = [x**2 for x in A]
print("Danh sách C:", C)

# c) 
D = random.sample([x for x in A if x % 3 == 0], k=min(len([x for x in A if x % 3 == 0]), n))
print("Danh sách D:", D)