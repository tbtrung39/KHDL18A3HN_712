n = int(input("Nhập số n (bậc của ma trận): "))
A = []
for i in range(n):
    hang = []
    for j in range(n):
        if i == j:
            hang.append(1)
        else:
            hang.append(0)
    A.append(hang)
print("Ma trận đơn vị bậc", n, ":")
for hang in A:
    print(hang)