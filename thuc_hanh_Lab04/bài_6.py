so_0 = "không"
so_1 = "một"
so_2 = "hai"
so_3 = "ba"
so_4 = "bốn"
so_5 = "năm"
so_6 = "sáu"
so_7 = "bảy"
so_8 = "tám"
so_9 = "chín"
so_chu = [so_0, so_1, so_2, so_3, so_4, so_5, so_6, so_7, so_8, so_9]
so = input("Nhập một số: ")
for chu_so in so:
    print(so_chu[int(chu_so)],end=' ') 
 

