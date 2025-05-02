def hoanvi(n):
    if n == 1:
        return [[1]]
    else:
        hoanvitruoc = hoanvi(n - 1)
        hoanvimoi = []
        for hoanvidon in hoanvitruoc:
            for i in range(n):
                hoanvimoi.append(hoanvidon[:i] + [n] + hoanvidon[i:])
        return hoanvimoi

so_n = 3
kq = hoanvi(so_n)
print(f"Các hoán vị của 1 đến {so_n} là: {kq}")