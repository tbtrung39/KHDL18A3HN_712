def nhap_ma_tran():
    n=int(input("N: "))
    return [list(map(int,input().split())) for _ in range(n)]
def in_ma_tran(m):
    for d in m: print(*d)
def chuyen_vi(m):
    return [list(d) for d in zip(*m)]
def la_doi_xung(m):
    return m==chuyen_vi(m)
