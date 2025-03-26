chuoi = input("Nhập chuỗi: ")
ky_tu_max = ""
do_dai_max = 0
ky_tu_hien_tai = ""
do_dai_hien_tai = 0
for i in range(len(chuoi)):
    if i == 0 or chuoi[i] == chuoi[i - 1]: 
        do_dai_hien_tai += 1
        ky_tu_hien_tai = chuoi[i]
    else:  
        if do_dai_hien_tai > do_dai_max:
            do_dai_max = do_dai_hien_tai
            ky_tu_max = ky_tu_hien_tai
        do_dai_hien_tai = 1
        ky_tu_hien_tai = chuoi[i]
if do_dai_hien_tai > do_dai_max:
    do_dai_max = do_dai_hien_tai
    ky_tu_max = ky_tu_hien_tai
print("Chuỗi ký tự dài nhất:", ky_tu_max * do_dai_max)
