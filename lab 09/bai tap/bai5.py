def hoan_vi(dsach):
    if len(dsach) == 1:
        return [dsach]
    
    hoan_vi_result = []
    for i in range(len(dsach)):
        phan_tu = dsach[i]
        phan_con_lai = dsach[:i] + dsach[i+1:]
        for hoan_vi_con in hoan_vi(phan_con_lai):
            hoan_vi_result.append([phan_tu] + hoan_vi_con)
    return hoan_vi_result

def permutation(n):
    dsach = list(range(1, n + 1))
    return hoan_vi(dsach)

n = int(input("Nhap so n: "))
kq = permutation(n)
print("Cac hoan vi cua dsach tu 1 den", n, "la:", kq)