#Bai8
luong_can_ban=1350000
tham_nien_cong_tac=int(input("Nhập thâm niên công tác: "))
if tham_nien_cong_tac<12:
    he_so=2.34
elif tham_nien_cong_tac<36:
    he_so=3.33
elif tham_nien_cong_tac<60:
    he_so=3.66
else:
    he_so=3.99
luong=he_so*luong_can_ban
print("Lương của nhân viên là:", luong, "đồng.")
