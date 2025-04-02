chuoi_mat_khau=input("nhap mat khau: ")
mat_khau_kiem_tra=chuoi_mat_khau.split(',')
mat_khau_hop_le=[]
for i in mat_khau_kiem_tra:
    i=i.strip()
    thuong=False
    for a in i:
        if a.islower():
            thuong=True
            break
    hoa=False
    for a in i:
        if a.isupper():
            hoa=True
            break
    so=False
    for a in i:
        if a.isdigit():
            so=True
            break
    ki_tu_dac_biet=False
    for a in i:
        if a in "$#@":
            ki_tu_dac_biet=True
            break
    do_dai=6<=len(i)<=12
    if thuong and hoa and so and ki_tu_dac_biet:
        mat_khau_hop_le.append(i)
print(f"mật khẩu hợp lệ: {mat_khau_hop_le}")