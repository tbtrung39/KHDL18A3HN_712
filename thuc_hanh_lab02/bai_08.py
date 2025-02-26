luong_can_ban = 1350000
tham_nien_ct = int(input("Nhập thâm niên công tác của nhân viên (tháng): "))
if tham_nien_ct < 12:
    he_so = 2.34
elif 12 <= tham_nien_ct < 36:
    he_so = 3.33
elif 36 <= tham_nien_ct < 60:
    he_so = 3.66
else:
    he_so = 3.99
luong = he_so * luong_can_ban
print(f"Lương của nhân viên là: {luong:.2f} đồng")
