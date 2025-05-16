import doicoso2

print("=== CHƯƠNG TRÌNH CHUYỂN ĐỔI CƠ SỐ ===")
chuoi_nhap = input("Nhập chuỗi số: ")
chuoi_sau_loai = doicoso2.loai_bo_ky_tu_khong_hop_le(chuoi_nhap)
print("Chuỗi sau khi loại bỏ ký tự không hợp lệ:", chuoi_sau_loai)
co_so = doicoso2.kiem_tra_co_so(chuoi_sau_loai)
print(f"Cơ số của chuỗi này là: {co_so}")
if co_so == 2:
    print("Chuyển từ cơ số 2 sang cơ số 10:", doicoso2.chuyen_2_sang_10(chuoi_sau_loai))
elif co_so == 8:
    print("Chuyển từ cơ số 8 sang cơ số 10:", doicoso2.chuyen_8_sang_10(chuoi_sau_loai))
elif co_so == 16:
    print("Chuyển từ cơ số 16 sang cơ số 10:", doicoso2.chuyen_16_sang_10(chuoi_sau_loai))
else:
    print("Chuyển từ cơ số 10 sang cơ số 10:", chuoi_sau_loai)