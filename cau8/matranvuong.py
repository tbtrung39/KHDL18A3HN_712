def nhap_matran(N):
    matran = []
    print(f"Nhap ma tran {N}x{N}:")
    for i in range(N):
        hang = []
        for j in range(N):
            x = int(input(f"Nhap A[{i}][{j}]: "))
            hang.append(x)
        matran.append(hang)
    return matran
def in_matran(matran):
    for hang in matran:
        print(" ".join(map(str, hang)))
def chuyen_vi(matran):
    N = len(matran)
    return [[matran[j][i] for j in range(N)] for i in range(N)]
def kiem_tra_doi_xung(matran):
    N = len(matran)
    for i in range(N):
        for j in range(N):
            if matran[i][j] != matran[j][i]:
                return False
    return True
