chu_ngu=["Anh","Em"]
dong_tu=["Choi","Yêu"]
tan_ngu=["Bóng đá","Bóng rổ"]
list=[]
for chu in chu_ngu:
        for dong in dong_tu:
            for tan in tan_ngu:
                cau_moi=f"{chu} {dong} {tan}"
                list.append(cau_moi)
for cau in list:
    print(cau)