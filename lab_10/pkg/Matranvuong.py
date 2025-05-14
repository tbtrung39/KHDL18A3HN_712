def nhap_ma_tran(n):
    matrix = []
    print(f"Nhập các phần tử cho ma trận {n}x{n}:")
    for i in range(n):
        row = list(map(int, input(f"Hàng {i+1}: ").split()))
        while len(row) != n:
            print("Vui lòng nhập đúng số lượng phần tử.")
            row = list(map(int, input(f"Hàng {i+1}: ").split()))
        matrix.append(row)
    return matrix

def in_ma_tran(matrix):
    print("Ma trận:")
    for row in matrix:
        print(" ".join(map(str, row)))

def chuyen_vi(matrix):
    n = len(matrix)
    transposed = [[matrix[j][i] for j in range(n)] for i in range(n)]
    return transposed

def kiem_tra_doi_xung(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True
