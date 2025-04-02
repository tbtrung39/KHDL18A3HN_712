x, y = map(int, input("Nhập x và y: ").split())
matrix = [[i * j for j in range(y)] for i in range(x)]
print(matrix)