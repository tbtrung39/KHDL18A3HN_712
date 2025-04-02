#Bai14
ds_mat_khau = input("Nhập danh sách mật khẩu: ").split(",")
ky_tu_db = "%@$"
ds_mat_khau_hop_le = []
for mat_khau in ds_mat_khau:
    mat_khau = mat_khau.strip()
    if 6 <= len(mat_khau) <= 12:
        chu_thuong = False
        chu_hoa = False
        chu_so = False
        ky_tu_dac_biet = False
        for char in mat_khau:
            if 'a' <= char <= 'z':
                chu_thuong = True
            elif 'A' <= char <= 'Z':
                chu_hoa = True
            elif '0' <= char <= '9':
                chu_so = True
            elif char in ky_tu_db:
                ky_tu_dac_biet = True
        if chu_thuong and chu_hoa and chu_so and ky_tu_dac_biet:
            ds_mat_khau_hop_le.append(mat_khau)
print(",".join(ds_mat_khau_hop_le))