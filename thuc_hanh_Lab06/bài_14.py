import re
chuoi_mat_khau = input("Nhập chuỗi mật khẩu (phân tách bởi dấu phẩy): ")
danh_sach_mat_khau = chuoi_mat_khau.split(",")
mat_khau_hop_le = []
for mat_khau in danh_sach_mat_khau:
    mat_khau = mat_khau.strip()
    if len(mat_khau) < 6 or len(mat_khau) > 12:
        continue  
    co_chu_thuong = re.search("[a-z]", mat_khau)
    co_so = re.search("[0-9]", mat_khau)
    co_chu_hoa = re.search("[A-Z]", mat_khau)
    co_ky_tu_dac_biet = re.search("[$#@]", mat_khau)
    if co_chu_thuong and co_so and co_chu_hoa and co_ky_tu_dac_biet:
        mat_khau_hop_le.append(mat_khau)
print(",".join(mat_khau_hop_le))