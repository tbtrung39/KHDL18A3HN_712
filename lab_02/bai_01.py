#cau1:
thang = int(input("Nhập tháng:"))
if thang < 1 or thang > 12:
    print("Nhập sai , vui lòng nhập lại")
else:
    if thang == 2:
        print("Tháng 2 có 28 ngày (Năm không nhuận) \n 29 ngày (Năm không nhuận)")
    elif thang <= 7:
        if thang %2 == 0:
            print("Tháng",thang,"có 30 ngày")
        else:
            print("Tháng",thang,"có 31 ngày")
    else:
        if thang %2 == 0:
            print("Tháng",thang,"có 31 ngày")
        else:
            print("Tháng",thang,"có 30 ngày")