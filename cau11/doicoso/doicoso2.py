def loc_chuoi(chuoi):
    hop_le = "0123456789ABCDEFabcdef"
    ket_qua = ""
    for ky_tu in chuoi:
        if ky_tu in hop_le:
            ket_qua += ky_tu.upper()
    return ket_qua
def he2_sang_he10(chuoi):
    try:
        return int(chuoi, 2)
    except ValueError:
        return "Chuoi khong hop le cho he 2"
def he8_sang_he10(chuoi):
    try:
        return int(chuoi, 8)
    except ValueError:
        return "Chuoi khong hop le cho he 8"
def he16_sang_he10(chuoi):
    try:
        return int(chuoi, 16)
    except ValueError:
        return "Chuoi khong hop le cho he 16"
