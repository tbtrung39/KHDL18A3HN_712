tnct = int(input("nhập thâm niên công tác:"))
if tnct <12:
    luong1 = 2.34*1350000
    print("lương của nhân viên là:",luong1)
elif 12<=tnct<36:
    luong2 = 3.33*1350000
    print("lương của nhân viên là:",luong2)
elif 26<=tnct<60:
    luong3 = 3.66*1350000
    print("lương của nhân viên là:",luong3)
elif tnct>=36:
    luong4 = 3.99*1350000
    print("lương của nhân viên là:",luong4)
else:
    print("không hợp lệ vui lòng nhập lại")