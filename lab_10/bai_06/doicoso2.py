def loc_ky_tu_hop_le(chuoi):
    tap_hop_le = set("0123456789ABCDEF")
    return ''.join([ky_tu.upper() for ky_tu in chuoi if ky_tu.upper() in tap_hop_le])

def xac_dinh_he_co_so(chuoi):
    chuoi = chuoi.upper()
    if all(ky_tu in '01' for ky_tu in chuoi):
        return 2
    elif all(ky_tu in '01234567' for ky_tu in chuoi):
        return 8
    elif all(ky_tu in '0123456789ABCDEF' for ky_tu in chuoi):
        return 16
    else:
        return -1

def chuyen_sang_thap_phan(chuoi, he_co_so):
    try:
        return int(chuoi, he_co_so)
    except ValueError:
        return None

if __name__ == "__main__":
    chuoi_nhap = input("Nhap chuoi ky tu: ")
    chuoi_loc = loc_ky_tu_hop_le(chuoi_nhap)
    print("Chuoi hop le sau khi loc:", chuoi_loc)

    co_so = xac_dinh_he_co_so(chuoi_loc)
    if co_so == -1:
        print("Khong xac dinh duoc he co so.")
    else:
        print(f"Chuoi bieu dien theo he co so {co_so}")
        gia_tri_thap_phan = chuyen_sang_thap_phan(chuoi_loc, co_so)
        print(f"Gia tri thap phan tuong ung: {gia_tri_thap_phan}")
