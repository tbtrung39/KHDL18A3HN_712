def ktra_ky_tu(chuoi):
    tap_ky_tu = "0123456789ABCDEF"
    ket_qua = []
    for c in chuoi:
        if c.upper() not in tap_ky_tu:
            ket_qua.append(c)
    return ket_qua
def he_co_so_cua_chuoi(chuoi):
    chuoi = chuoi.upper()
    for c in chuoi:
        if c not in "01":
            break
    else:
        return 2
    for c in chuoi:
        if c not in "01234567":
            break
    else:
        return 8
    for c in chuoi:
        if c not in "0123456789":
            break
    else:
        return 10
    for c in chuoi:
        if c not in "0123456789ABCDEF":
            break
    else:
        return 16
    return -1 
def doi_co_so_sang_10(chuoi, co_so):
    return int(chuoi, base=co_so)