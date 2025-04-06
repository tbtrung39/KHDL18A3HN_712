chuoi_ky_tu = input("Nhập vào chuỗi ký tự: ")
dic_chuoi_con = {}
for do_dai in range(1, len(chuoi_ky_tu) + 1):
    for vi_tri in range(len(chuoi_ky_tu) - do_dai + 1):
        chuoi_con = chuoi_ky_tu[vi_tri:vi_tri+do_dai]
        if chuoi_con in dic_chuoi_con:
            dic_chuoi_con[chuoi_con] += 1
        else:
            dic_chuoi_con[chuoi_con] = 1
print("Từ điển các chuỗi con và số lần xuất hiện:")
print(dic_chuoi_con)
