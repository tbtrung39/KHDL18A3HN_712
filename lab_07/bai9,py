n = int(input("Nhập một số tự nhiên n: "))
A = []
B = []
for i in range(2, n):
    nguyen_to = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            nguyen_to = False
            break
    if nguyen_to and n % i == 0:
        if i not in A:
            A.append(i)
    if nguyen_to and n % i != 0:
        if i not in B:
            B.append(i)
A = set(A)
B = set(B)
print("Tập hợp A (các số nguyên tố là ước của n):", A if A else 0)
print("Tập hợp B (các số nguyên tố nhỏ hơn n và không phải là ước của n):", B if B else 0)
####
# print("Tập hợp A (các số nguyên tố là ước của n):", A)
# print("Tập hợp B (các số nguyên tố nhỏ hơn n và không phải là ước của n):", B)