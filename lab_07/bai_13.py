chuoi_kt = input("Nhap chuoi ky tu: ")
chuoi_con = {}
for i in range(1, len(chuoi_kt) + 1):
    for vi_tri in range(len(chuoi_kt) - i + 1):
        chuoi_con = chuoi_kt[vi_tri:vi_tri+i]
        if chuoi_con in chuoi_con:
            chuoi_con[chuoi_con] += 1
        else:
            chuoi_con[chuoi_con] = 1
print("Từ điển các chuỗi con và số lần xuất hiện:")
print(chuoi_con)