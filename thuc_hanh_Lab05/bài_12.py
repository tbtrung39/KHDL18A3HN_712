chuoi = input("Nhập chuỗi ký tự: ")
tu_hien_tai = ""  
danh_sach_tu = []  
for ky_tu in chuoi:
    if ky_tu != " " and ky_tu != ",": 
        tu_hien_tai += ky_tu 
    else:
        if tu_hien_tai: 
            danh_sach_tu = danh_sach_tu + [tu_hien_tai]  
            tu_hien_tai = ""  
if tu_hien_tai:
    danh_sach_tu = danh_sach_tu + [tu_hien_tai]  
for tu in danh_sach_tu:
    print(tu)