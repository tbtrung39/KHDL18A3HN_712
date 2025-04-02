import random
A = [random.randint(1, 99999) for _ in range(1000)]
# Cách 1: Sử dụng hàm sorted()
A_sorted_1 = sorted(A)
print("List A sau khi sắp xếp (cách 1 - sorted()):", A_sorted_1[:10])
# Cách 2: Không sử dụng hàm sorted()
A_sorted_2 = A[:] 
n = len(A_sorted_2)
for i in range(n):
    for j in range(0, n - i - 1):
        if A_sorted_2[j] > A_sorted_2[j + 1]:
            A_sorted_2[j], A_sorted_2[j + 1] = A_sorted_2[j + 1], A_sorted_2[j]
print("List A sau khi sắp xếp (cách 2 - Bubble Sort):", A_sorted_2[:10])
