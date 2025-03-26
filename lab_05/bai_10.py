Str1 = input("Nhap chuoi ky tu Str1: ")
Str2 = input("Nhap chuoi ky tu Str2: ")
do_dai_cuc_dai = ""
for i in range(len(Str1)):
    for j in range(i+1, len(Str1)+1):
        kt = Str1[i:j]
        if kt in Str2 and len(kt)>len(do_dai_cuc_dai):
            do_dai_cuc_dai = kt
if do_dai_cuc_dai:
    print("Chuoi con chung dai nhat la:", do_dai_cuc_dai)
else:
    print("Khong co chuoi con chung!")
