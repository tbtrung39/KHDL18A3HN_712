#Bai6
import random
def hoan_vi_ngau_nhien(n):
    A = list(range(1, n + 1))
    kq = []
    while len(A) > 0:
        chi_so = random.randint(0, len(A) - 1)
        kq.append(A[chi_so])
        A.pop(chi_so)
    return kq
n = int(input("Nhập n: "))
print("Hoán vị ngẫu nhiên của dãy số từ 1 đến n là:", hoan_vi_ngau_nhien(n))