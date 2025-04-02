import random
A = [random.randint(1, 99999) for _ in range(1000)]
print("List A (10 phần tử đầu):", A[:10])  
A_sorted_1 = sorted(A)
print("List A sau khi sắp xếp (cách 1 - sorted()):", A_sorted_1[:10])


