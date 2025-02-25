loai_xe = int(input("Nhập loại xe (4 hoặc 7): "))
km_di_duoc = float(input("Nhập quãng đường đã đi (km): "))
thoi_gian_cho = int(input("Nhập thời gian chờ (phút): "))
if loai_xe == 4:
    gia_mo_cua = 11000 
    quang_duong_mien_phi = 0.8  
    gia_trong_pham_vi_20km = 12100  
    gia_sau_21km = 10000 
    if km_di_duoc <= 0.8:
        cuoc_taxi = gia_mo_cua
    elif km_di_duoc <= 20:
        cuoc_taxi = gia_mo_cua + (km_di_duoc - quang_duong_mien_phi) * gia_trong_pham_vi_20km
    else:
        cuoc_taxi = gia_mo_cua + (20 - quang_duong_mien_phi) * gia_trong_pham_vi_20km + (km_di_duoc - 20) * gia_sau_21km
elif loai_xe == 7:
    gia_mo_cua = 13000  
    quang_duong_mien_phi = 0.8  
    gia_trong_pham_vi_30km = 14100  
    gia_sau_31km = 12000  
    if km_di_duoc <= 0.8:
        cuoc_taxi = gia_mo_cua
    elif km_di_duoc <= 30:
        cuoc_taxi = gia_mo_cua + (km_di_duoc - quang_duong_mien_phi) * gia_trong_pham_vi_30km
    else:
        cuoc_taxi = gia_mo_cua + (30 - quang_duong_mien_phi) * gia_trong_pham_vi_30km + (km_di_duoc - 30) * gia_sau_31km
    if thoi_gian_cho > 5:
        thoi_gian_cho_thuc_te = thoi_gian_cho - 5  
        cuoc_taxi += thoi_gian_cho_thuc_te * 800  
print(f"Cước taxi phải trả: {cuoc_taxi} đồng.")
