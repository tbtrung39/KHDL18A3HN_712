import random
A = []
while True:
    n = int(input("Nhập số nguy hiểm (nhập 0 để dừng): "))
    if n == 0:
        break
    A.append(n)
B = []
for x in A:
    if x % 3 == 0 and x % 5 != 0:
        B.append(x)
print("Danh sách B (chia hết cho 3 nhưng không chia hết cho 5):", B)
C = []
for x in A:
    C.append(x**2)
print("Danh sách C (bình phương của A):", C)
D_candidates = []
for x in A:
    if x % 3 == 0:
        D_candidates.append(x)
D = random.sample(D_candidates, min(len(D_candidates), 3)) if D_candidates else []
print("Danh sách D (ngẫu nhiên từ A, chia hết cho 3):", D)