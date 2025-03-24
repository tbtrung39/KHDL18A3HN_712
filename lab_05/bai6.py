# cau 6
c_ky_tu = input("Nhập chuỗi ký tự: ")
he_hex = ""
la_hex = True  
for ky_tu in c_ky_tu:
    if ky_tu not in he_hex:
        la_hex = False  
        break  
if la_hex:
    print("Chuỗi nhập vào là hệ Hex hợp lệ.")
else:
    print("Chuỗi nhập vào không hoàn toàn là hệ Hex")
    chuoi_hex = ""
    for ky_tu in c_ky_tu:
        if ky_tu in he_hex:
            chuoi_hex += ky_tu  
    if chuoi_hex == "":
        print("ky tu khong hop le va khong the chuyen doi")
    else:
        so_thap_phan = int(chuoi_hex, 16)
        print("Chuoi hex hop le la:", chuoi_hex)
        print("Giá trị thập phan la:", so_thap_phan)
