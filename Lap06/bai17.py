n = int(input("Nhập bậc n của ma trận đơn vị: "))
 matrix = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
 for row in matrix:
     print(row)