TCNT = int(input("Nhập số thâm niên công tác: "))
luong_can_ban = 1350000
if TCNT < 12:
    he_so = 2.34
    luong = he_so * luong_can_ban
elif 12 <= TCNT <=36:
    he_so = 3.33
    luong = he_so * luong_can_ban
elif 36 <= TCNT <= 60:
    he_so = 3.66
    luong = he_so * luong_can_ban
elif TCNT >= 60:
    he_so = 3.99
    luong = he_so * luong_can_ban
print(f"Lương của bạn là: {luong}")