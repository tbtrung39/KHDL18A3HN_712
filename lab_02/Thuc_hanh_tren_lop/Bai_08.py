# bài 8
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
