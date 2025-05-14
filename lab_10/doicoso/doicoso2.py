def xoa_ky_tu_khong_hop_le(chuoi):
    valid_chars = "03247346HBHGG"
    result = ''.join([char for char in chuoi if char in valid_chars])
    print("chuoi sau khi loai bo ko hl: " + result)

def kiem_tra_co_so(chuoi):
    if all(char in "01" for char in chuoi):
        print("chuoi da nhap co co so 2.")
    elif all(char in "01234567" for char in chuoi):
        print("chuoi da nhap co co so 8.")
    elif all(char in "0123456789ABCDEF" for char in chuoi):
        print("chuoi da nhap co co so 16.")
    else:
        print("chuoi ko hl.")

def chuyen_sang_co_so_10(chuoi, co_so):
    if co_so == 2:
        if all(char in "01" for char in chuoi):
            so_10 = 0
            for i, char in enumerate(reversed(chuoi)):
                so_10 += int(char) * (2 ** i)
            print(f"Số {chuoi} o co so 2 chuyen sang co so 10 la: {so_10}")
        else:
            print("chuoi khong hop le")
    
    elif co_so == 8:
        if all(char in "01234567" for char in chuoi):
            so_10 = 0
            for i, char in enumerate(reversed(chuoi)):
                so_10 += int(char) * (8 ** i)
            print(f"so{chuoi} o co so 8 chuyen sang co so 10 la: {so_10}")
        else:
            print("chuoi ko hop le")
    
    elif co_so == 16:
        #ktra xem chuoi da hop le chua
        if all(char in "0123456789ABCDEF" for char in chuoi):
            so_10 = 0
            for i, char in enumerate(reversed(chuoi)):
                if char.isdigit():
                    so_10 += int(char) * (16 ** i)
                else:
                    so_10 += (ord(char.upper()) - 55) * (16 ** i)
            print(f"so {chuoi} o co so 16 chuyen sang co so 10 la: {so_10}")
        else:
            print("chuoi ko hop le")
