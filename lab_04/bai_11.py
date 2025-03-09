print("                      CHƯƠNG TRÌNH GỌI ĐỒ UỐNG                   ")
print(' _________________________________________________________________')
print("|                          Menu chọn đồ uống                      |")
print("|1.         Cafe                                                  |")
print("|2.         Cam vắt                                               |")
print("|3.         Nước ép cà rốt                                        |")
print("|4.         Nước lọc                                              |")
print("|5.         Nước dừa                                              |")
print('|_________________________________________________________________|')
chon = 0  

while chon < 1 or chon > 5:
    chon = int(input("Nhập số tương ứng với đồ uống bạn muốn chọn: "))

    if chon == 1:
        print("Bạn đã chọn cafe")
    elif chon == 2:
        print("Bạn đã chọn cam vắt")
    elif chon == 3:
        print("Bạn đã chọn nước ép cà rốt")
    elif chon == 4:
        print("Bạn đã chọn nước lọc")
    elif chon == 5:
        print("Bạn đã chọn nước dừa")
    else:
        print("Số thứ tự không hợp lệ! Vui lòng nhập lại.")