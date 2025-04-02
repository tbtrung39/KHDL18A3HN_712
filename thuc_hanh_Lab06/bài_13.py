chu_ngu = ["Anh", "Em"]
dong_tu = ["Chơi", "Yêu"]
tan_ngu = ["Bóng đá", "Bóng rổ"]
cac_cau = [f"{cn} {dt} {tn}." for cn in chu_ngu for dt in dong_tu for tn in tan_ngu]
for cau in cac_cau:
    print(cau)