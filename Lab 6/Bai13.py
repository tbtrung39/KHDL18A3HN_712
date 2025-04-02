#Bai13
ds_chu_ngu = ["Anh", "Em"]
ds_dong_tu = ["Chơi", "Yêu"]
ds_tan_ngu = ["Bóng đá", "Bóng rổ"]
for chu_ngu in ds_chu_ngu:
    for dong_tu in ds_dong_tu:
        for tan_ngu in ds_tan_ngu:
            cau_hoan_chinh = f"{chu_ngu} {dong_tu} {tan_ngu}"
            print(cau_hoan_chinh)