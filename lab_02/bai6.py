so_nguyen = int(input("Nhập vào một số nguyên có ba chữ số: "))
hang_tram = so_nguyen // 100
hang_chuc = (so_nguyen % 100) // 10
hang_don_vi = so_nguyen % 10
if hang_tram == 1:
    chu_tram = "một trăm"
elif hang_tram == 2:
    chu_tram = "hai trăm"
elif hang_tram == 3:
    chu_tram = "ba trăm"
elif hang_tram == 4:
    chu_tram = "bốn trăm"
elif hang_tram == 5:
    chu_tram = "năm trăm"
elif hang_tram == 6:
    chu_tram = "sáu trăm"
elif hang_tram == 7:
    chu_tram = "bảy trăm"
elif hang_tram == 8:
    chu_tram = "tám trăm"
elif hang_tram == 9:
    chu_tram = "chín trăm"

if hang_chuc == 1:
    chu_chuc = "mười"
elif hang_chuc == 2:
    chu_chuc = "hai mươi"
elif hang_chuc == 3:
    chu_chuc = "ba mươi"
elif hang_chuc == 4:
    chu_chuc = "bốn mươi"
elif hang_chuc == 5:
    chu_chuc = "năm mươi"
elif hang_chuc == 6:
    chu_chuc = "sáu mươi"
elif hang_chuc == 7:
    chu_chuc = "bảy mươi"
elif hang_chuc == 8:
    chu_chuc = "tám mươi"
elif hang_chuc == 9:
    chu_chuc = "chín mươi"
elif hang_chuc == 0:
    chu_chuc = "lẻ"

if hang_don_vi == 1:
    chu_don_vi = "một"
elif hang_don_vi == 2:
    chu_don_vi = "hai"
elif hang_don_vi == 3:
    chu_don_vi = "ba"
elif hang_don_vi == 4:
    chu_don_vi = "bốn"
elif hang_don_vi == 5:
    chu_don_vi = "năm"
elif hang_don_vi == 6:
    chu_don_vi = "sáu"
elif hang_don_vi == 7:
    chu_don_vi = "bảy"
elif hang_don_vi == 8:
    chu_don_vi = "tám"
elif hang_don_vi == 9:
    chu_don_vi = "chín"
elif hang_don_vi == 0:
    chu_don_vi = ""

if hang_chuc == 0 and hang_don_vi == 0:
    chu_so = chu_tram
elif hang_chuc == 0:
    chu_so = f"{chu_tram} lẻ {chu_don_vi}"
else:
    chu_so = f"{chu_tram} {chu_chuc} {chu_don_vi}"
print(f"{so_nguyen} đọc là: {chu_so}")
