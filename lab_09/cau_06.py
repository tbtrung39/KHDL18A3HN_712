import random

def hoan_vi_ngau_nhien(n):
    A = list(range(1, n + 1))
    result = []
    while A:
        phan_tu = random.choice(A)
        result.append(phan_tu)
        A.remove(phan_tu)
    return result

n = int(input("Nhập số tự nhiên n: "))
result = hoan_vi_ngau_nhien(n)
print("Hoán vị ngẫu nhiên của dãy [1, 2, ..., n] là:", result)
