import doicoso2 

chuoi = input("Nhap chuoi ki tu tu ban phim: ")
chuoi_sau_khi_loai = doicoso2.xoa_ky_tu_khong_hop_le(chuoi)
doicoso2.kiem_tra_co_so(chuoi_sau_khi_loai)

doicoso2.chuyen_sang_co_so_10(chuoi_sau_khi_loai, 2)
doicoso2.chuyen_sang_co_so_10(chuoi_sau_khi_loai, 8)
doicoso2.chuyen_sang_co_so_10(chuoi_sau_khi_loai, 16)