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