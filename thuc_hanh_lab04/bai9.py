so = input("hay nhap so: ") 
s= 0
kt = True
for chu_so in so:
    if chu_so == "0":
        s += 0
    elif chu_so == "1":
        s += 1
    elif chu_so == "2":
        s += 2
    elif chu_so == "3":
        s += 3
    elif chu_so == "4":
        s += 4
    elif chu_so == "5":
        s += 5
    elif chu_so == "6":
        s += 6
    elif chu_so == "7":
        s += 7
    elif chu_so == "8":
        s += 8
    elif chu_so == "9":
        s += 9
    elif chu_so == "-":
        continue  
    else:
        print("Số nhập không hợp lệ")
        kt=False
        break
if kt:
    print("Tổng các chữ số là:", )