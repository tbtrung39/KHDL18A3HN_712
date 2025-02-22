so_nguyen = int(input("Nhập vào một số nguyên có ba chữ số: "))

if so_nguyen >= 100 or so_nguyen <= -100:
    hang_tram = so_nguyen // 100
    hang_chuc = (so_nguyen // 10) % 10
    hang_don_vi = so_nguyen % 10
    
    if so_nguyen < 0:
        print("Âm", end=" ")
        hang_tram = -hang_tram
    
    if hang_tram == 1:
        print("một trăm", end=" ")
    elif hang_tram == 2:
        print("hai trăm", end=" ")
    elif hang_tram == 3:
        print("ba trăm", end=" ")
    elif hang_tram == 4:
        print("bốn trăm", end=" ")
    elif hang_tram == 5:
        print("năm trăm", end=" ")
    elif hang_tram == 6:
        print("sáu trăm", end=" ")
    elif hang_tram == 7:
        print("bảy trăm", end=" ")
    elif hang_tram == 8:
        print("tám trăm", end=" ")
    elif hang_tram == 9:
        print("chín trăm", end=" ")
    
    if hang_chuc == 0 and hang_don_vi != 0:
        print("lẻ", end=" ")
    elif hang_chuc == 1:
        print("mười", end=" ")
    elif hang_chuc == 2:
        print("hai mươi", end=" ")
    elif hang_chuc == 3:
        print("ba mươi", end=" ")
    elif hang_chuc == 4:
        print("bốn mươi", end=" ")
    elif hang_chuc == 5:
        print("năm mươi", end=" ")
    elif hang_chuc == 6:
        print("sáu mươi", end=" ")
    elif hang_chuc == 7:
        print("bảy mươi", end=" ")
    elif hang_chuc == 8:
        print("tám mươi", end=" ")
    elif hang_chuc == 9:
        print("chín mươi", end=" ")
    
    if hang_don_vi == 1 and hang_chuc > 1:
        print("mốt")
    elif hang_don_vi == 2:
        print("hai")
    elif hang_don_vi == 3:
        print("ba")
    elif hang_don_vi == 4:
        print("bốn")
    elif hang_don_vi == 5:
        print("năm")
    elif hang_don_vi == 6:
        print("sáu")
    elif hang_don_vi == 7:
        print("bảy")
    elif hang_don_vi == 8:
        print("tám")
    elif hang_don_vi == 9:
        print("chín")
else:
    print("Vui lòng nhập một số nguyên có đúng ba chữ số.")
