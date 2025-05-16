def nhap_ma_tran(N):
    ma_tran = []
    for i in range(N):
        hang = list(map(int, input(f"Nhập các phần tử của hàng {i+1} (cách nhau bởi dấu phẩy): ").split(",")))
        ma_tran.append(hang)
    return ma_tran

def in_ma_tran(ma_tran):
    for hang in ma_tran:
        print(" ".join(map(str, hang)))

def ma_tran_chuyen_vi(ma_tran):
    return [[ma_tran[j][i] for j in range(len(ma_tran))] for i in range(len(ma_tran[0]))]

def kiem_tra_doi_xung(ma_tran):
    n = len(ma_tran)
    for i in range(n):
        for j in range(n):
            if ma_tran[i][j] != ma_tran[j][i]:
                return False
    return True
