luong_can_ban = 1350000
tnct = int(input("Nhập vào thâm niên công tác (tháng): "))

if tnct < 12:
    he_so = 2.34
elif 12 <= tnct < 36:
    he_so = 3.33
elif 36 <= tnct < 60:
    he_so = 3.66
elif tnct >= 60:
    he_so = 3.99
else: 
    print("Giá trị không hợp lệ")
luong = he_so * luong_can_ban
print("Lương của nhân viên là: ", luong)