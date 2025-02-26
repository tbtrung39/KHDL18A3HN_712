so = int(input("Nhập vào một số nguyên có ba chữ số: "))
# Kiểm tra xem số có đúng ba chữ số không
if (so >= 100 and so <= 999) or (so <= -100 and so >= -999):
    if so < 0:
        am = "âm "
        so = -so  
    else:
        am = "" 
    hang_tram = so // 100
    hang_chuc = (so // 10) % 10
    hang_don_vi = so % 10
    don_vi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]
    tram = ["", "một trăm", "hai trăm", "ba trăm", "bốn trăm", "năm trăm", "sáu trăm", "bảy trăm", "tám trăm", "chín trăm"]
    if hang_chuc == 0 and hang_don_vi == 0:
        doc = f"{tram[hang_tram]}"
    elif hang_chuc == 1 and hang_don_vi == 0:
        doc = f"{tram[hang_tram]} mười"
    else:
        if hang_don_vi == 0:
            doc = f"{tram[hang_tram]} {chuc[hang_chuc]}"
        else:
            doc = f"{tram[hang_tram]} {chuc[hang_chuc]} {don_vi[hang_don_vi]}"
    doc = am + doc
    print(f"Cách đọc: {doc}")
else:
    print("Vui lòng nhập số nguyên có ba chữ số.")

