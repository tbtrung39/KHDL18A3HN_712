print("Menu đồ uống:")
print("1. Cafe")
print("2. Cam vắt")
print("3. Nước ép cà rốt")

while True:
    chon = input("Nhập số tương ứng với đồ uống bạn muốn chọn: ")
    hop_le = True
    j = 0

    while j < len(chon):  
        if not ("0" <= chon[j] <= "9"):  
            hop_le = False
            break
        j += 1  

    if hop_le and chon:
        chon = int(chon)
        if chon == 1:
            print("Bạn đã chọn Cafe.")
            break
        elif chon == 2:
            print("Bạn đã chọn Cam vắt.")
            break
        elif chon == 3:
            print("Bạn đã chọn Nước ép cà rốt.")
            break

    print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
