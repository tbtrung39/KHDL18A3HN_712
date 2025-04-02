
chu_ngu = ["Anh", "Em"]
dong_tu = ["Chơi", "Yêu"]
tan_ngu = ["Bóng đá", "Bóng rổ"]
cau = []
for cn in chu_ngu:
    for dt in dong_tu:
        for tn in tan_ngu:
            cau.append(cn + " " + dt + " " + tn)
print("Tất cả các câu có thể:")
for c in cau:
    print(c)