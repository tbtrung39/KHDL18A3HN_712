def nhap_matran(n):
    return [[int(input(f"Nhập phần tử M[{i}][{j}]: ")) for j in range(n)] for i in range(n)]
def in_matran(M):
    for row in M:
        print(' '.join(map(str, row)))
def chuyen_vi(M):
    return [[M[j][i] for j in range(len(M))] for i in range(len(M))]
def kiem_tra_doi_xung(M):
    return M == chuyen_vi(M)