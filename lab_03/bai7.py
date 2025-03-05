n = int(input("Nhap so nguyen duong n: "))
S = 0
for i in range(1, n + 1):
    S = S + 1/i
print(S, end = " ")