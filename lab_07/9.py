n = int(input("Nhập số nguyên n: "))
A = set()
B = set()
for i in range(1, n+1):
    if n % i == 0:
        A.add(i)
    if i % n == 0:
        B.add(i)
print("Tập A (ước của n):", A)
print("Tập B (bội của n từ 1 đến n):", B)