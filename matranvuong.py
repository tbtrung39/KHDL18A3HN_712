#Bai 8
def nhap_ma_tran(N):
    ma_tran = []
    for i in range(N):
        row = []
        for j in range(N):
            while True:
                try:
                    print("Nhap ma tran tai vi tri [{}][{}]:".format(i+1, j+1))
                    x = int(input())
                    row.append(x)
                    break
                except ValueError:
                    print("Hay nhap mot so nguyen!")
        ma_tran.append(row)
    return ma_tran

def in_ma_tran(ma_tran):
    for row in ma_tran:
        print(" ".join(map(str, row)))

def ma_tran_chuyen_vi(ma_tran):
    N = len(ma_tran)
    chuyen_vi = [[ma_tran[j][i] for j in range(N)] for i in range(N)]
    return chuyen_vi

def kiem_tra_doi_xung(ma_tran):
    N = len(ma_tran)
    for i in range(N):
        for j in range(N):
            if ma_tran[i][j] != ma_tran[j][i]:
                return False
    return True