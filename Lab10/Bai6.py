import doicoso2
chuoi = input("Nhap chuoi ky tu: ").strip()
ky_tu_sai = doicoso2.ktra_ky_tu(chuoi)
if ky_tu_sai:
    print("Ky tu khong hop le:", ky_tu_sai)
else:
    he = doicoso2.he_co_so_cua_chuoi(chuoi)
    if he == -1:
        print("Khong the xac dinh he co so.")
    else:
        print("Chuoi thuoc he co so:",he)
        print("Gia tri thap phan:", doicoso2.doi_co_so_sang_10(chuoi, he))