password = input("Nhap mat khau: ")

if 6 <= len(password) <= 12:
    co_chu_thuong = False
    co_chu_hoa = False
    co_so = False
    co_ky_tu_dac_biet = False

    for char in password:
        if 'a' <= char <= 'z':  
            co_chu_thuong = True
        elif 'A' <= char <= 'Z':  
            co_chu_hoa = True
        elif '0' <= char <= '9':  
            co_so = True
        elif char in "$#@": 
            co_ky_tu_dac_biet = True

    if co_chu_thuong and co_chu_hoa and co_so and co_ky_tu_dac_biet:
        print("Mat khau hop le!")
    else:
        print("Mat khau khong hop le!")
else:
    print("Mat khau khong hop le!")