n = int(input("Nhập số nguyên có ba chữ số: "))
if 100 <= n <= 999:
    hang_tram = n // 100
    hang_chuc = (n // 10) % 10
    hang_don_vi = n % 10
    #số hàng trăm
    so_hang_tram = ""
    if hang_tram == 1:
        so_hang_tram = "một"
    elif hang_tram == 2:
        so_hang_tram = "hai"
    elif hang_tram == 3:
        so_hang_tram = "ba"
    elif hang_tram == 4:
        so_hang_tram = "bốn"
    elif hang_tram == 5:
        so_hang_tram = "năm"
    elif hang_tram == 6:
        so_hang_tram = "sáu"
    elif hang_tram == 7:
        so_hang_tram = "bảy"
    elif hang_tram == 8:
        so_hang_tram = "tám"
    elif hang_tram == 9:
        so_hang_tram = "chín"
    #Số hàng chục
    so_hang_chuc = ""
    if hang_chuc == 1:
        so_hang_chuc = "mười"
    elif hang_chuc == 2:
        so_hang_chuc = "hai mươi"
    elif hang_chuc == 3:
        so_hang_chuc = "ba mươi"
    elif hang_chuc == 4:
        so_hang_chuc = "bốn mươi"
    elif hang_chuc == 5:
        so_hang_chuc = "năm mươi"
    elif hang_chuc == 6:
        so_hang_chuc = "sáu mươi"
    elif hang_chuc == 7:
        so_hang_chuc = "bảy mươi"
    elif hang_chuc == 8:
        so_hang_chuc = "tám mươi"
    elif hang_chuc == 9:
        so_hang_chuc = "chín mươi"
    #Số hàng đơn vị
    so_hang_don_vi = ""
    if hang_don_vi == 1:
        so_hang_don_vi = "một"
    elif hang_don_vi == 2:
        so_hang_don_vi = "hai"
    elif hang_don_vi == 3:
        so_hang_don_vi = "ba"
    elif hang_don_vi == 4:
        so_hang_don_vi = "bốn"
    elif hang_don_vi == 5:
        so_hang_don_vi = "năm"
    elif hang_don_vi == 6:
        so_hang_don_vi = "sáu"
    elif hang_don_vi == 7:
        so_hang_don_vi = "bảy"
    elif hang_don_vi == 8:
        so_hang_don_vi = "tám"
    elif hang_don_vi == 9:
        so_hang_don_vi = "chín"
    cach_doc = f"{so_hang_tram} trăm {so_hang_chuc} {so_hang_don_vi}"
    print("Cách đọc của số nguyên", n, "là:", cach_doc)
else:
    print("Số nhập vào không phải là số nguyên có ba chữ số.")    