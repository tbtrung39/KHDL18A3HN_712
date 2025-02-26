x = float(input("nhập số giờ thuê:"))
if x<3:
    tien1 = x*100000
    print("tiền thuê sân là:",tien1)
elif 3<x<11:
    tien2 = 3*(100000)+(x-3)*(100000*0.25)
    print("tiền thuê sân là:",tien2)
elif 11<=x<15:
    tien3 = (3*(100000*0.25)+(x-3)*(100000*0.25))-((3*(100000*0.25)+(x-3)*(100000*0.25))*0.1)
    print("tiền thuê sân là:",tien3)
else:
    print("không hợp lệ vui lòng nhập lại")