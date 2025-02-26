TNCT = int(input("Nhập thâm niên công tác (tháng): "))
lcb = 1350000
if TNCT < 12:
    hs = 2.34
elif TNCT < 36:
    hs = 3.33
elif TNCT < 60:
    hs = 3.66
else:
    hs = 3.99
luong = hs * lcb
print(f"Lương: {luong} đồng")
