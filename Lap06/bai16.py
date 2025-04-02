X, Y = map(int, input("Nhập X và Y: ").split())
 matrix = [[i * j for j in range(Y)] for i in range(X)]
 print(matrix)