x = int(input("nhập số điện tiêu thụ:"))
if 0<x<100:
    tien1 = 2000*x
    print("tiền điện tháng này là:",tien1)
elif 101<x<200:
    tien2 = 2500*x
    print("tiền diện tháng này là:",tien2)
elif 201<x<300:
    tien3 = 3000*x
    print("tiền điện tháng này là:",tien3)
elif x>300:
    tien4 = 5000*x
    print("tiền điện tháng này là:",tien4)
else:
    print("không hơp lệ vui lòng nhập lại")