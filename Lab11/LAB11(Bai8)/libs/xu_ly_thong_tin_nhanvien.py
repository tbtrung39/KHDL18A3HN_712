def tinh_luong(he_so_luong):
    return he_so_luong*1490000
def tinh_phu_cap(chuc_vu):
    if chuc_vu.upper()=="TP":
        return 1000000
    elif chuc_vu.upper()=="PP":
        return 700000
    elif chuc_vu.upper()=="NV":
        return 300000
    else:
        return 0
def tinh_thuc_linh(he_so_luong, chuc_vu):
    return tinh_luong(he_so_luong) + tinh_phu_cap(chuc_vu)