# bai 4
def hoan_vi(dsach, vtri):
    if vtri == len(dsach):
        print(dsach)
        return
    else:
        for i in range(vtri, len(dsach)):
            dsach[vtri], dsach[i] = dsach[i], dsach[vtri]
            hoan_vi(dsach, vtri + 1)
            dsach[vtri], dsach[i] = dsach[i], dsach[vtri]

n = int(input("Nhập số tự nhiên n: "))
dsach = list(range(1, n + 1))
hoan_vi(dsach, 0)
