#Bai10
n = input("Nhập số n: ")  
if not n.isdigit:  
    print("Nhập sai, vui lòng nhập lại!")  
else:  
    so_n=str(n)  
    chuoi_chu_so = " "  
    for i in so_n:  
        if i == ".":  
            chu_so = "phẩy"  
        elif i == "0":  
            chu_so = "không"  
        elif i == "1":  
            chu_so = "một"  
        elif i == "2":  
            chu_so = "hai"  
        elif i == "3":  
            chu_so = "ba"  
        elif i == "4":  
            chu_so = "bốn"  
        elif i == "5":  
            chu_so = "năm"  
        elif i == "6":  
            chu_so = "sáu"  
        elif i == "7":  
            chu_so = "bảy"  
        elif i == "8":  
            chu_so = "tám"  
        else:  
            chu_so = "chín"  
        chuoi_chu_so += chu_so + " "  
    print("Số", n, "viết dưới dạng ký tự là:", chuoi_chu_so)