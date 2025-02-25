so_hang = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
n = int(input("Nhập một số nguyên có ba chữ số: "))
if 100 <= abs(n) <= 999:
    tram = abs(n) // 100
    chuc = (abs(n) // 10) % 10
    don_vi = abs(n) % 10
    
    ket_qua = so_hang[tram] + " trăm "
    if chuc == 0 and don_vi != 0:
        ket_qua += "lẻ "
    elif chuc == 1:
        ket_qua += "mười "
    elif chuc > 1:
        ket_qua += so_hang[chuc] + " mươi "
    
    if don_vi == 1 and chuc > 1:
        ket_qua += "mốt"
    elif don_vi == 5 and chuc > 0:
        ket_qua += "lăm"
    elif don_vi > 0:
        ket_qua += so_hang[don_vi]
    
    if n < 0:
        ket_qua = "Âm " + ket_qua
    
    print("Cách đọc:", ket_qua.strip())
else:
    print("Số không hợp lệ! Vui lòng nhập số có đúng ba chữ số.")