#Bai10
str1 = input("Nhập chuỗi Str1: ")
str2 = input("Nhập chuỗi Str2: ")
chuoi_con_dai_nhat = ' '
for i in range(len(str1)):
    for j in range(i + 1, len(str1) + 1):
        chuỗi_con = str1[i:j]
        if chuoi_con in str2 and len(chuoi_con) > len(chuoi_con_dai_nhat):
            chuoi_con_dai_nhat = chuoi_con
if chuoi_con_dai_nhat:
    print("Chuỗi con chung dài nhất của", str1, "và", str2, "là:", chuoi_con_dai_nhat)
else:
    print("Chuỗi", str1, "và", str2, "không có chuỗi con chung nào")