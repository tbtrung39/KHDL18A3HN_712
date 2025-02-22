# bài 11
# Chương trình tìm ngày tiếp theo của một ngày cho trước
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
# Xác định số ngày trong tháng
if thang in [1, 3, 5, 7, 8, 10, 12]:
    so_ngay_trong_thang = 31
elif thang in [4, 6, 9, 11]:
    so_ngay_trong_thang = 30
elif thang == 2:
    so_ngay_trong_thang = 28
else:
    so_ngay_trong_thang = -1  # Tháng không hợp lệ
# Kiểm tra ngày hợp lệ
if so_ngay_trong_thang == -1 or ngay < 1 or ngay > so_ngay_trong_thang:
    print("Ngày hoặc tháng không hợp lệ. Vui lòng nhập lại.")
else:
    # Tính ngày tiếp theo
    if ngay < so_ngay_trong_thang:
        ngay_tiep_theo = ngay + 1
        thang_tiep_theo = thang
    else:
        ngay_tiep_theo = 1
        if thang == 12:
            thang_tiep_theo = 1  # Chuyển sang tháng 1 năm sau
        else:
            thang_tiep_theo = thang + 1
    print(f"Ngày tiếp theo là: {ngay_tiep_theo}/{thang_tiep_theo}")
