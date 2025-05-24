def nhap_ma_tran(n):
    matran = []
    for i in range(n):
        while True:
            dong = input("Nhap dong",i+1, "gom",n,"so:")
            gtri = dong.strip().split()
            if len(gtri) != n:
                print("Sai so luong phan tu, vui long nhap lai!!!")
                continue
            row = [int(x) for x in gtri]
            matran.append(row)
            break
    return matran
def tinh_tong(matran):
    return sum(sum(row) for row in matran)
def kiem_tra_doi_xung(matran):
    n = len(matran)
    for i in range(n):
        for j in range(n):
            if matran[i][j] != matran[j][i]:
                return False
    return True