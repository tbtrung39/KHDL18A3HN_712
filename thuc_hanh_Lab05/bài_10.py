chuoi_1 = input("Nhập chuỗi thứ nhất: ")
chuoi_2 = input("Nhập chuỗi thứ hai: ")
do_dai_max = 0
chuoi_con_dai_nhat = ""
for bat_dau in range(len(chuoi_1)):
    for ket_thuc in range(bat_dau, len(chuoi_1)):
        chuoi_con = chuoi_1[bat_dau:ket_thuc + 1]  
        if chuoi_con in chuoi_2 and len(chuoi_con) > do_dai_max:
            do_dai_max = len(chuoi_con)
            chuoi_con_dai_nhat = chuoi_con  
print("Chuỗi con chung dài nhất là:", chuoi_con_dai_nhat)
