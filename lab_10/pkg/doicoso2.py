def loc_ky_tu_hop_le(chuoi):
    hop_le = set("0123456789ABCDEF")
    return ''.join([c.upper() for c in chuoi if c.upper() in hop_le])

def xac_dinh_he_co_so(chuoi):
    chuoi = chuoi.upper()
    if all(c in '01' for c in chuoi):
        return 2
    elif all(c in '01234567' for c in chuoi):
        return 8
    elif all(c in '0123456789ABCDEF' for c in chuoi):
        return 16
    else:
        return -1  

def chuyen_doi_sang_thap_phan(chuoi, co_so):
    try:
        return int(chuoi, co_so)
    except ValueError:
        return None

if __name__ == "__main__":
    chuoi_nhap = input("Nhập chuỗi ký tự: ")
    chuoi_loc = loc_ky_tu_hop_le(chuoi_nhap)
    print("Chuỗi hợp lệ sau khi lọc:", chuoi_loc)

    he_co_so = xac_dinh_he_co_so(chuoi_loc)
    if he_co_so == -1:
        print("Không xác định được hệ cơ số.")
    else:
        print(f"Chuỗi biểu diễn theo hệ cơ số {he_co_so}")
        gia_tri_thap_phan = chuyen_doi_sang_thap_phan(chuoi_loc, he_co_so)
        print(f"Giá trị thập phân tương ứng: {gia_tri_thap_phan}")
