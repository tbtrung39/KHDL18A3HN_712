def tinh_luong(nhanvien):
    """
    nhan dict nhan vien co 'hesoluong' va 'chucvu',
    tinh 'luong', 'phucap', 'thuclinh' roi cap nhat lai dict.
    """
    he_so_luong = float(nhanvien.get('hesoluong', 0))
    chuc_vu = nhanvien.get('chucvu', '').upper()

    luong = he_so_luong * 1490000

    if chuc_vu == 'TP':
        phu_cap = 1000000
    elif chuc_vu == 'PP':
        phu_cap = 700000
    elif chuc_vu == 'NV':
        phu_cap = 300000
    else:
        phu_cap = 0

    thuc_linh = luong + phu_cap

    nhanvien['luong'] = luong
    nhanvien['phucap'] = phu_cap
    nhanvien['thuclinh'] = thuc_linh


def sap_xep_giam_dan_theo_thuclinh(danh_sach_nv):
    """
    sap xep danh sach nhan vien giam dan theo thuclinh.
    danh_sach_nv la list cac dict nhan vien.
    """
    return sorted(danh_sach_nv, key=lambda nv: nv.get('thuclinh', 0), reverse=True)
