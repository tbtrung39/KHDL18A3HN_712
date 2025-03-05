chuoi_container = input("Nhập chuỗi container (10 ký tự): ").upper()

if len(chuoi_container) != 10:
    print("Chuỗi container không hợp lệ. Vui lòng nhập chuỗi 10 ký tự.")
else:
    trong_so = []
    for i, ky_tu in enumerate(chuoi_container):
        if ky_tu.isalpha():  
            ma_ascii = ord(ky_tu) - ord('A')  
            if ma_ascii < 9:
                gia_tri = ma_ascii + 10
            elif ma_ascii < 22:
                gia_tri = ma_ascii + 11
            else:
                gia_tri = ma_ascii + 12
        else:  
            gia_tri = int(ky_tu)
        trong_so.append(gia_tri * (2 ** i))
tong_trong_so = sum(trong_so)
so_kiem_tra = tong_trong_so % 11
print("Số kiểm tra container là:", so_kiem_tra)