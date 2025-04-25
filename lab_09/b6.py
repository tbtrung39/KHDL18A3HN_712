# bai 6
import random
def hoan_vi_ngau_nhien(n):
    A = list(range(1, n + 1))
    result = []
    for _ in range(n):
        phan_tu = random.choice(A)
        result.append(phan_tu)
        A.remove(phan_tu)
    return result

n = int(input("Nhap so tu nhien n: "))
result = hoan_vi_ngau_nhien(n)
print("Hoan vi ngau nhien cua day so tu 1 den", n, "la:", result)
