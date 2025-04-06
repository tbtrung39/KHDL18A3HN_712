#Bai5
import random
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
A = set()
while len(A) < 5:
    A.add(random.choice(lst))
print("Tập hợp A: ", A)