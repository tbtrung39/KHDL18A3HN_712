# câu 9
so = input("hay nahp so: ")
tong = 0
hop_le = True
for chu_so in so:
    if chu_so == "0":
        tong += 0
    elif chu_so == "1":
        tong += 1
    elif chu_so == "2":
        tong += 2
    elif chu_so == "3":
        tong += 3
    elif chu_so == "4":
        tong += 4
    elif chu_so == "5":
        tong += 5
    elif chu_so == "6":
        tong += 6
    elif chu_so == "7":
        tong += 7
    elif chu_so == "8":
        tong += 8
    elif chu_so == "9":
        tong += 9
    elif chu_so == "-":
        continue  
    else:
        print("Số nhập không hợp lệ")
        hop_le = False
        break
if hop_le:
    print("Tổng các chữ số là:", tong)
