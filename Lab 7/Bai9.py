#Bai9
n = int(input("Nhập số tự nhiên n: "))
A = set()
B = set()
for i in range(2, n + 1):
    ktra_ngto = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            ktra_ngto = False
            break
    if ktra_ngto and n % i == 0:
        A.add(i)
for i in range(2, n):
    ktra_ngto = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            ktra_ngto = False
            break
    if ktra_ngto and n % i != 0:
        B.add(i)
print("Tập hợp A:", A)
print("Tập hợp B:", B)