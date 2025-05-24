str1=input("Hay nhap chuoi thu nhat: ")
str2=input("Hay nhap chuoi thu hai: ")
len_str1 = len(str1)
len_str2 = len(str2)
chuoi_con_dai_nhat = ""
i=0
while i < len_str1:
    j=i+1
    while j <= len_str1:
        chuoi_con = str1[i:j]
        if chuoi_con in str2 and len(chuoi_con) > len(chuoi_con_dai_nhat):
            chuoi_con_dai_nhat = chuoi_con
        j += 1
    i += 1
print("Chuoi con chung dai nhat cua hai chuoi da nhap la: ",chuoi_con_dai_nhat)