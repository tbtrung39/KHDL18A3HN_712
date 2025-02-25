num = int(input("Nhập vào một số nguyên có ba chữ số: "))

if 100 <= num <= 999:
    hang_tram = num // 100
    hang_chuc = (num // 10) % 10
    hang_dv = num % 10

    chu_so = ["Không", "Một", "Hai", "Ba", "Bốn", "Năm", "Sáu", "Bảy", "Tám", "Chín"]

    if hang_tram == 1:
        tram_text = "Một trăm"
    elif hang_tram == 2:
        tram_text = "Hai trăm"
    elif hang_tram == 3:
        tram_text = "Ba trăm"
    elif hang_tram == 4:
        tram_text = "Bốn trăm"
    elif hang_tram == 5:
        tram_text = "Năm trăm"
    elif hang_tram == 6:
        tram_text = "Sáu trăm"
    elif hang_tram == 7:
        tram_text = "Bảy trăm"
    elif hang_tram == 8:
        tram_text = "Tám trăm"
    else:
        tram_text = "Chín trăm"

    if hang_chuc == 0 and hang_dv != 0:
        chuc_text = "lẻ"
    elif hang_chuc == 1:
        chuc_text = "mười"
    elif hang_chuc == 2:
        chuc_text = "hai mươi"
    elif hang_chuc == 3:
        chuc_text = "ba mươi"
    elif hang_chuc == 4:
        chuc_text = "bốn mươi"
    elif hang_chuc == 5:
        chuc_text = "năm mươi"
    elif hang_chuc == 6:
        chuc_text = "sáu mươi"
    elif hang_chuc == 7:
        chuc_text = "bảy mươi"
    elif hang_chuc == 8:
        chuc_text = "tám mươi"
    elif hang_chuc == 9:
        chuc_text = "chín mươi"
    else:
        chuc_text = ""

    if hang_dv == 1 and hang_chuc > 1:
        dv_text = "mốt"
    elif hang_dv == 5 and hang_chuc > 0:
        dv_text = "lăm"
    elif hang_dv == 0:
        dv_text = ""
    else:
        dv_text = chu_so[hang_dv]

    print(tram_text, chuc_text, dv_text)
else:
    print("Số nhập vào không hợp lệ, vui lòng nhập số có ba chữ số.")
