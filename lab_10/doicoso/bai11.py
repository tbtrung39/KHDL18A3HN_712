import doicoso1    

so = doicoso1.nhap_so()
doicoso1.chuyen_sang_nhi_phan(so)
doicoso1.chuyen_sang_bat_phan(so)
doicoso1.chuyen_sang_thap_luc_phan(so)

import doicoso2 

chuoi = input("nhap chui ki tu tu ban phim: ")
chuoi_sau_khi_loai = doicoso2.xoa_ky_tu_khong_hop_le(chuoi)
doicoso2.kiem_tra_co_so(chuoi_sau_khi_loai)
# chuyen doi
doicoso2.chuyen_sang_co_so_10(chuoi_sau_khi_loai, 2)
doicoso2.chuyen_sang_co_so_10(chuoi_sau_khi_loai, 8)
doicoso2.chuyen_sang_co_so_10(chuoi_sau_khi_loai, 16)
