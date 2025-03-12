so = input("Nhập một số: ")
for chu_so in so:
    if chu_so == "0":
        print("không", end=" ")
    elif chu_so == "1":
        print("một", end=" ")
    elif chu_so == "2":
        print("hai", end=" ")
    elif chu_so == "3":
        print("ba", end=" ")
    elif chu_so == "4":
        print("bốn", end=" ")
    elif chu_so == "5":
        print("năm", end=" ")
    elif chu_so == "6":
        print("sáu", end=" ")
    elif chu_so == "7":
        print("bảy", end=" ")
    elif chu_so == "8":
        print("tám", end=" ")
    elif chu_so == "9":
        print("chín", end=" ")
    elif chu_so == "-":
        print("âm", end=" ")  
    else:
        print(" không hợp lệ!")
        break
else:
    print()