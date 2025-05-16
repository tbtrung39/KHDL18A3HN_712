def loai_bo_ky_tu_khong_hop_le(chuoi):
    ky_tu_hop_le = "0123456789ABCDEF"
    chuoi_sau = "".join(c for c in chuoi.upper() if c in ky_tu_hop_le)
    return chuoi_sau

def kiem_tra_co_so(chuoi):
    for c in chuoi:
        if c in "ABCDEF":
            return 16
    return 10

def chuyen_2_sang_10(chuoi):
    return int(chuoi, 2)

def chuyen_8_sang_10(chuoi):
    return int(chuoi, 8)

def chuyen_16_sang_10(chuoi):
    return int(chuoi, 16)
