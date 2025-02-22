#cau6:
a = int(input("Nhập 1 số nguyên có 3 chữ số"))
if a < 100 or a > 999:
    print("Nhập sai số nguyên có 3 chữ số")
else:
    hang_tram = a // 100
    hang_chuc = (a // 10) % 10
    hang_don_vi = a % 10
    print("Số nguyên trên đọc là:", hang_tram , "trăm" , hang_chuc , "mươi" , hang_don_vi )