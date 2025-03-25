chuoi1 = input("Nhập chuỗi ký tự thứ nhất: ")
chuoi2 = input("Nhập chuỗi ký tự thứ hai: ")

do_dai_max = 0
chuoi_con_dai_nhat = ""

for i in range(len(chuoi1)):
    for j in range(i + 1, len(chuoi1) + 1):
        chuoi_con = chuoi1[i:j]
        if chuoi_con in chuoi2 and len(chuoi_con) > do_dai_max:
            do_dai_max = len(chuoi_con)
            chuoi_con_dai_nhat = chuoi_con

if chuoi_con_dai_nhat:
    print("Chuỗi con chung dài nhất là:", chuoi_con_dai_nhat)
else:
    print("Không có chuỗi con chung.")
