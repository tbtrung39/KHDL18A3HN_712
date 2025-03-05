#phan a
n = int(input("nhập số hàng của tam giác 1: "))
for i in range(n):
    for j in range(i + 1):
        if j == 0 or j == i or i == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()

        

#phanb

n = int(input("Nhập số dòng của tam giác2: "))
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i or i == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#phan c
n = int(input("nhập số hàng của tam giác 2:"))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))