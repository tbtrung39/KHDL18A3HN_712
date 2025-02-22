#cau11:
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
if thang > 12 or thang < 1:
    print("Nhập sai, Vui lòng nhập lại")
else:
    if thang == 2:
        if ngay == 28:
            ngay = 1
            thang += 1
            print("Ngày tiếp theo là: ","ngày",ngay,"tháng",thang)
        elif ngay < 1 or ngay > 28:
            print("Nhập sai , tháng 2 có 28 ngày")
        else:
            ngay += 1
            print("Ngày tiếp theo là: ","ngày",ngay,"tháng",thang)
    elif thang <= 7:
        if thang %2 == 0:
            if ngay == 30:
                ngay = 1
                thang += 1
                print("Ngày tiếp theo là: ","ngày",ngay,"tháng",thang)
            elif thang %2 != 0:
                ngay += 1
                print("Ngày tiếp theo là: ","ngày",ngay,"tháng",thang)
            else: print("Nhập sai")
        else:
            if ngay == 31:
                ngay = 1
                thang += 1
                print("Ngày tiếp theo là: ","ngày",ngay,"tháng",thang)
            else:
                ngay += 1
                print("Ngày tiếp theo là: ","ngày",ngay,"tháng",thang)
    elif thang < 12:
        if thang %2 == 0:
            if ngay == 31:
                ngay = 1
                thang += 1
                print("Ngày tiếp theo là: ","ngày",ngay,"tháng",thang)
            else:
                ngay += 1
                print("Ngày tiếp theo là: ","ngày",ngay,"tháng",thang)
        else:
            if ngay == 30:
                ngay = 1
                thang += 1
                print("Ngày tiếp theo là: ","ngày",ngay,"tháng",thang)
            else:
                ngay += 1
                print("Ngày tiếp theo là: ","ngày",ngay,"tháng",thang)
    else:  
        if ngay == 12:
            ngay = 1
            thang = 1
            print("Ngày tiếp theo là: ","ngày",ngay,"tháng",thang)
        else:
            ngay += 1
            print("Ngày tiếp theo là: ","ngày",ngay,"tháng",thang)