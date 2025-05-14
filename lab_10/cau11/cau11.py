from doicoso import doicoso1, doicoso2

print("=== CHƯƠNG TRÌNH CHUYỂN ĐỔI CƠ SỐ ===")
lua_chon = input("1. Nhập số nguyên\n2. Nhập chuỗi ký tự\nChọn: ")

if lua_chon == "1":
    so = doicoso1.nhap_so_nguyen()
    print(f"Số vừa nhập: {so}")
    print(f"Nhị phân: {doicoso1.doi_nhi_phan(so)}")
    print(f"Bát phân: {doicoso1.doi_bat_phan(so)}")
    print(f"Thập lục phân: {doicoso1.doi_thap_luc_phan(so)}")

elif lua_chon == "2":
    chuoi = input("Nhập chuỗi ký tự: ")
    chuoi_hop_le = doicoso2.loai_bo_ky_tu_khong_hop_le(chuoi)
    print(f"Chuỗi sau khi loại bỏ ký tự không hợp lệ: {chuoi_hop_le}")
    co_so = doicoso2.kiem_tra_co_so(chuoi_hop_le)
    print(f"Cơ số của chuỗi này là: {co_so}")
    if co_so == 2:
        print("Giá trị hệ 10:", doicoso2.chuyen_2_sang_10(chuoi_hop_le))
    elif co_so == 8:
        print("Giá trị hệ 10:", doicoso2.chuyen_8_sang_10(chuoi_hop_le))
    elif co_so == 16:
        print("Giá trị hệ 10:", doicoso2.chuyen_16_sang_10(chuoi_hop_le))
    else:
        print("Giá trị hệ 10:", chuoi_hop_le)