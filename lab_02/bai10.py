luong = float(input("Nhập lương của nhân viên (triệu đồng): "))
if luong > 15:
    thue = luong * 0.30
elif 7 <= luong <= 15:
    thue = luong * 0.20
else:
    thue = luong * 0.10
luong_thuc_nhan = luong - thue
print(f"Lương trước thuế: {luong} triệu đồng.")
print(f"Thuế thu nhập: {thue} triệu đồng.")
print(f"Lương thực nhận sau thuế: {luong_thuc_nhan} triệu đồng.")
