# bài 6
so_nguyen = int(input("Nhập số nguyên có ba chữ số: "))
ten_so = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
if 100 <= abs(so_nguyen) <= 999:
    tram = abs(so_nguyen) // 100
    chuc = (abs(so_nguyen) // 10) % 10
    don_vi = abs(so_nguyen) % 10
    ket_qua = ten_so[tram] + " trăm "
    if chuc == 0 and don_vi == 0:
        ket_qua += ""
    elif chuc == 0:
        ket_qua += "lẻ " + ten_so[don_vi]
    elif chuc == 1:
        ket_qua += "mười " + ten_so[don_vi]
    else:
        ket_qua += ten_so[chuc] + " mươi " + ten_so[don_vi]
    if so_nguyen < 0:
        ket_qua = "Âm " + ket_qua
    print("Cách đọc số:", ket_qua)
else:
    print("Số không hợp lệ! Vui lòng nhập số có ba chữ số.")
