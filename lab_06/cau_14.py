danh_sach_mat_khau = input("Nhập danh sách mật khẩu, cách nhau bởi dấu phẩy: ").split(",")
mat_khau_hop_le = []
for mat_khau in danh_sach_mat_khau:
    mat_khau = mat_khau.strip()
    if 6 <= len(mat_khau) <= 12:
        co_chu_thuong = co_chu_hoa = co_so = co_ky_tu_dac_biet = False
        for ky_tu in mat_khau:
            if "a" <= ky_tu <= "z":
                co_chu_thuong = True
            elif "A" <= ky_tu <= "Z":
                co_chu_hoa = True
            elif "0" <= ky_tu <= "9":
                co_so = True
            elif ky_tu in "$#@":
                co_ky_tu_dac_biet = True
        if co_chu_thuong and co_chu_hoa and co_so and co_ky_tu_dac_biet:
            mat_khau_hop_le.append(mat_khau)
print(",".join(mat_khau_hop_le))