import os
print('\n CHƯƠNG TRÌNH CHỌN ĐỒ UỐNG.')
while True:
    print(' _________________________________________')
    print("|           Menu chọn đồ uống             |")
    print("|[1] Cafe                                 |")
    print("|[2] Cam vắt                              |")
    print("|[3] Nước ép cà rốt                       |")
    print("|[4] Nước lọc                             |")
    print("|[5] Nước dừa                             |")
    print('|_________________________________________|')

    chon=int(input("Chọn đồ uống mà bạn cần:"))
    if chon ==1:
        print("Bạn đã chọn đồ uống cafe")
    elif chon ==2:
        print("Bạn đã chọn đồ uống cam vắt")
    elif chon ==3:
        print("Bạn đã chọn đồ uống nước ép cà rốt")
    elif chon ==4:
        print("Bạn đã chọn đồ uống nước lọc")
    elif chon ==5:
        print("Bạn đã chọn đồ uống nước dừa")
    elif chon == 0:
        break
    else:
        print("Không có trong menu đã cho sẵn")
    tt=input("Nhấn phím bất kỳ để tiếp tục,bấm số 0 để thoát.")
    if tt==0:
        break
    else:
        os.system('cls')
