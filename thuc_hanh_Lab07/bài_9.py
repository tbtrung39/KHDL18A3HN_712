n = int(input("Nhập số tự nhiên n: "))
A = set()
B = set()
for i in range(2, n):  
    la_nguyen_to = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            la_nguyen_to = False
            break
    if la_nguyen_to:
        if n % i == 0:
            A.add(i)  
        else:
            B.add(i)  
print("Tập A (ước nguyên tố của n):", A)
print("Tập B (nguyên tố < n, không là ước):", B)
