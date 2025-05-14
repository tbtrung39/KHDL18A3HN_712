def nhap_ma_tran(n):
    matran = []
    print(f"Nhập ma trận {n}x{n}:")
    for i in range(n):
        hang = []
        for j in range(n):
            x = int(input(f"Nhập phần tử hàng {i + 1}, cột {j + 1}: "))
            hang.append(x)
        matran.append(hang)
    return matran

def in_ma_tran(matran):
    print("Ma trận:")
    for hang in matran:
        for x in hang:
            print(x, end=' ')
        print()

def chuyen_vi(matran):
    n = len(matran)
    ket_qua = []
    for i in range(n):
        dong_moi = []
        for j in range(n):
            dong_moi.append(matran[j][i])
        ket_qua.append(dong_moi)
    return ket_qua

def la_ma_tran_doi_xung(matran):
    n = len(matran)
    for i in range(n):
        for j in range(n):
            if matran[i][j] != matran[j][i]:
                return False
    return True
