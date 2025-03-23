Str = input("Nhập chuỗi ký tự: ")
do_dai_chuoi = ""
chuoi_sau = ""
for i in range(len(Str)):
    if i == 0 or Str[i] == Str[i - 1]:  
        chuoi_sau += Str[i]
    else:  
        if len(chuoi_sau) > len(do_dai_chuoi):  
            do_dai_chuoi = chuoi_sau
        chuoi_sau = Str[i]  
if len(chuoi_sau) > len(do_dai_chuoi):
    do_dai_chuoi = chuoi_sau
print("Chuỗi ký tự con dài nhất:", do_dai_chuoi)
