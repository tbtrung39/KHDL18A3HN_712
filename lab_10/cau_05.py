import doicoso1

print("=== CHƯƠNG TRÌNH CHUYỂN ĐỔI CƠ SỐ ===")
so = doicoso1.nhap_so_nguyen()

print(f"Số vừa nhập: {so}")
print(f"Số ở hệ nhị phân (base 2): {doicoso1.doi_nhi_phan(so)}")
print(f"Số ở hệ bát phân (base 8): {doicoso1.doi_bat_phan(so)}")
print(f"Số ở hệ thập lục phân (base 16): {doicoso1.doi_thap_luc_phan(so)}")

