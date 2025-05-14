def nhap_ma_tran(n):
    return [[int(input(f"Nhap pt hang {i+1}, cot {j+1}: ")) for j in range(n)] for i in range(n)]

def in_ma_tran(m):
    for row in m:
        print(" ".join(map(str, row)))

def chuyen_vi(m):
    n = len(m)
    return [[m[j][i] for j in range(n)] for i in range(n)]

def doi_xung(m):
    return m == chuyen_vi(m)