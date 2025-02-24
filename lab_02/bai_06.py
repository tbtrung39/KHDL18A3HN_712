so = int(input("Nhap so nguyen co 3 chu so: "))

if 100 <= so <= 999:
    hang_tram = so // 100
    hang_chuc = (so % 100) // 10
    hang_don_vi = so % 10

    if hang_tram == 1:
        doc_tram = "một trăm"
    elif hang_tram == 2:
        doc_tram = "hai trăm"
    elif hang_tram == 3:
        doc_tram = "ba trăm"
    elif hang_tram == 4:
        doc_tram = "bốn trăm"
    elif hang_tram == 5:
        doc_tram = "năm trăm"
    elif hang_tram == 6:
        doc_tram = "sáu trăm"
    elif hang_tram == 7:
        doc_tram = "bảy trăm"
    elif hang_tram == 8:
        doc_tram = "tám trăm"
    elif hang_tram == 9:
        doc_tram = "chín trăm"

    if hang_chuc == 0:
        doc_chuc = "lẻ"
    elif hang_chuc == 1:
        doc_chuc = "mười"
    elif hang_chuc == 2:
        doc_chuc = "hai mươi"
    elif hang_chuc == 3:
        doc_chuc = "ba mươi"
    elif hang_chuc == 4:
        doc_chuc = "bốn mươi"
    elif hang_chuc == 5:
        doc_chuc = "năm mươi"
    elif hang_chuc == 6:
        doc_chuc = "sáu mươi"
    elif hang_chuc == 7:
        doc_chuc = "bảy mươi"
    elif hang_chuc == 8:
        doc_chuc = "tám mươi"
    elif hang_chuc == 9:
        doc_chuc = "chín mươi"

    if hang_don_vi == 0:
        doc_don_vi = ""
    elif hang_don_vi == 1:
        doc_don_vi = "một"
    elif hang_don_vi == 2:
        doc_don_vi = "hai"
    elif hang_don_vi == 3:
        doc_don_vi = "ba"
    elif hang_don_vi == 4:
        doc_don_vi = "bốn"
    elif hang_don_vi == 5:
        doc_don_vi = "năm"
    elif hang_don_vi == 6:
        doc_don_vi = "sáu"
    elif hang_don_vi == 7:
        doc_don_vi = "bảy"
    elif hang_don_vi == 8:
        doc_don_vi = "tám"
    elif hang_don_vi == 9:
        doc_don_vi = "chín"

    if hang_chuc == 0 and hang_don_vi == 0:
        print(f"Cách đọc của số {so} là: {doc_tram}")
    elif hang_chuc == 0:
        print(f"Cách đọc của số {so} là: {doc_tram} {doc_chuc} {doc_don_vi}")
    else:
        print(f"Cách đọc của số {so} là: {doc_tram} {doc_chuc} {doc_don_vi}")
else:
    print("Số nhập vào không hợp lệ. Vui lòng nhập số có ba chữ số.")