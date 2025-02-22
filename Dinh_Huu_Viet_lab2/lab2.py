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
#cau2:
import math
a = int(input("Nhập vào số a: "))
b = int(input("Nhập vào số b: "))
c = int(input("Nhập vào số c: "))
delta = b**2 - 4*a*c
if delta < 0:
    print("Phương trình vô nghiệm")
elif delta == 0:
    x = -b / (2 * a)
    print("Phương trình có nghiệm kép x =", x)
else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print("Phương trình có 2 nghiệm phân biệt:")
    print("x1 =", x1)
    print("x2 =", x2)
#cau3:
thu = int(input("Nhập thứ:"))
if thu > 7 or thu < 1:
    print("Nhập sai , Vui lòng nhập lại")
else:
    if thu == 1:print("1:Sunday")
    elif thu == 2:print("2: Monday")
    elif thu == 3:print("3: Tuesday")
    elif thu == 4:print("4: Wednesday")
    elif thu == 5:print("5:Thursday ")
    elif thu == 6:print("6: Friday")
    else:print("7: Saturday")
#cau4:
so_nguyen = int(input("Nhập vào một số nguyên: "))
if so_nguyen >= 100:
    chu_so_hang_tram = (so_nguyen // 100) % 10
    print("Chữ số hàng trăm là:", chu_so_hang_tram)
else:
    print("0")
#cau5:
thang = int(input("Nhập tháng: "))
if thang > 12 or thang < 1:
    print("Nhập sai, vui lòng nhập lại")
else:
    if thang == 1:
        print("1: January")
    elif thang == 2:
        print("2: February")
    elif thang == 3:
        print("3: March")
    elif thang == 4:
        print("4: April")
    elif thang == 5:
        print("5: May")
    elif thang == 6:
        print("6: June")
    elif thang == 7:
        print("7: July")
    elif thang == 8:
        print("8: August")
    elif thang == 9:
        print("9: September")
    elif thang == 10:
        print("10: October")
    elif thang == 11:
        print("11: November")
    else:
        print("12: December")
#cau6:
a = int(input("Nhập 1 số nguyên có 3 chữ số"))
if a < 100 or a > 999:
    print("Nhập sai số nguyên có 3 chữ số")
else:
    hang_tram = a // 100
    hang_chuc = (a // 10) % 10
    hang_don_vi = a % 10
    print("Số nguyên trên đọc là:", hang_tram , "trăm" , hang_chuc , "mươi" , hang_don_vi )
#cau7:
Diem_TK = float(input("Nhập điểm tổng kết: "))
if 0.0 <= Diem_TK <= 3.0:
    print("Loại Kém")
elif Diem_TK == 4.0:
    print("Loại Yếu")
elif 5.0 <= Diem_TK <= 6.0:
    print("Loại Trung bình")
elif 7.0 <= Diem_TK <= 8.0:
    print("Loại Khá")
elif 9.0 <= Diem_TK <= 10.0:
    print("Loại Giỏi")
else:
    print("Điểm không hợp lệ!")
#cau8:
luong_can_ban = 1350000
tham_nien_ct = int(input("Nhập số tháng thâm niên công tác: "))
if tham_nien_ct < 12:
    he_so = 2.34
elif 12 <= tham_nien_ct < 36:
    he_so = 3.33
elif 36 <= tham_nien_ct < 60:
    he_so = 3.66
else:
    he_so = 4.98
luong = he_so * luong_can_ban
print("Lương của nhân viên là:", luong, "đồng")
#cau9:
so_kw = int(input("Nhập số KW điện tiêu thụ: "))
if 0 <= so_kw <= 100:
    don_gia = 2000
elif 101 <= so_kw <= 200:
    don_gia = 2500
elif 201 <= so_kw <= 300:
    don_gia = 3000
else:
    don_gia = 5000
tien_dien = so_kw * don_gia
print("Tiền điện phải trả là:", tien_dien, "đồng")
#cau10:
gio_bat_dau = int(input("Nhập giờ bắt đầu (5-22): "))
gio_ket_thuc = int(input("Nhập giờ kết thúc (5-22): "))
if 5 <= gio_bat_dau <= gio_ket_thuc <= 22:
    thoi_gian_thue = gio_ket_thuc - gio_bat_dau
    if thoi_gian_thue <= 3:
        tien_thue = thoi_gian_thue * 100000
    else:
        tien_thue = 3 * 100000 + (thoi_gian_thue - 3) * 100000 * 0.75
    if 11 <= gio_bat_dau <= 15 and 11 <= gio_ket_thuc <= 15:
        tien_thue = tien_thue * 0.9
    print("Số tiền thuê sân là:", tien_thue, "đồng")
else:
    print("Giờ nhập vào không hợp lệ.")
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