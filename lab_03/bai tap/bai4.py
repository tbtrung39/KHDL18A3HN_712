import math
n = int(input("Nhập n: "))
so_nguyen_to = []
for i in range(2, n+1):
    nguyen_to = True
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            nguyen_to = False
            break
    if nguyen_to:
        so_nguyen_to.append(i)
print("Các số nguyên tố nhỏ hơn hoặc bằng n:", so_nguyen_to)