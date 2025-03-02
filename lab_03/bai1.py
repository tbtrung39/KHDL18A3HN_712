print("Nhập mã container gồm 10 ký tự:")
tong_trong_so = 0  
hop_le = True  
for i in range(10):
    ky_tu = input("Nhập ký tự thứ " + str(i + 1) + ": ")  
    if ky_tu == 'A':
        gia_tri = 10
    elif ky_tu == 'B':
        gia_tri = 12
    elif ky_tu == 'C':
        gia_tri = 13
    elif ky_tu == 'D':
        gia_tri = 14
    elif ky_tu == 'E':
        gia_tri = 15
    elif ky_tu == 'F':
        gia_tri = 16
    elif ky_tu == 'G':
        gia_tri = 17
    elif ky_tu == 'H':
        gia_tri = 18
    elif ky_tu == 'I':
        gia_tri = 19
    elif ky_tu == 'J':
        gia_tri = 20
    elif ky_tu == 'K':
        gia_tri = 21
    elif ky_tu == 'L':
        gia_tri = 23
    elif ky_tu == 'M':
        gia_tri = 24
    elif ky_tu == 'N':
        gia_tri = 25
    elif ky_tu == 'O':
        gia_tri = 26
    elif ky_tu == 'P':
        gia_tri = 27
    elif ky_tu == 'Q':
        gia_tri = 28
    elif ky_tu == 'R':
        gia_tri = 29
    elif ky_tu == 'S':
        gia_tri = 30
    elif ky_tu == 'T':
        gia_tri = 31
    elif ky_tu == 'U':
        gia_tri = 32
    elif ky_tu == 'V':
        gia_tri = 34
    elif ky_tu == 'W':
        gia_tri = 35
    elif ky_tu == 'X':
        gia_tri = 36
    elif ky_tu == 'Y':
        gia_tri = 37
    elif ky_tu == 'Z':
        gia_tri = 38
    elif ky_tu >= '0' and ky_tu <= '9':  
        gia_tri = int(ky_tu)
    else:
        print("Ký tự không hợp lệ! Dừng chương trình.")
        hop_le = False  
        break  
    if hop_le:
        tong_trong_so = tong_trong_so + gia_tri * (2 ** i)
if hop_le:
    so_kiem_tra = tong_trong_so % 11
    print("Số kiểm tra của container là:", so_kiem_tra)
