chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]

so = ""
while True:
    so = input("Nhập số nguyên dương: ")
    i = 0
    hop_le = True

    while i < len(so):
        if so[i] not in "0123456789":  
            hop_le = False
            break
        i += 1

    if hop_le and len(so) > 0:  
        break
    print("Vui lòng nhập số nguyên dương hợp lệ!")

i = 0
ket_qua = ""
while i < len(so):
    if so[i] == "0":
        so_nguyen = 0
    elif so[i] == "1":
        so_nguyen = 1
    elif so[i] == "2":
        so_nguyen = 2
    elif so[i] == "3":
        so_nguyen = 3
    elif so[i] == "4":
        so_nguyen = 4
    elif so[i] == "5":
        so_nguyen = 5
    elif so[i] == "6":
        so_nguyen = 6
    elif so[i] == "7":
        so_nguyen = 7
    elif so[i] == "8":
        so_nguyen = 8
    else:
        so_nguyen = 9

    ket_qua += chu_so[so_nguyen] + " "  
    i += 1

print("Kết quả:", ket_qua)
