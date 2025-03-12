import os
print('\n    CHƯƠNG TRÌNH GỌI ĐỒ UỐNG.   ')
while True:
    print('_________________________________________')
    print("|           Menu chọn đồ uống:          |")
    print("|[1] Cafe                               |")
    print("|[2] Cam vắt                            |")
    print("|[3] Nước ép cà rốt                     |")
    print("|[4] Nước lọc                           |")
    print("|[5] Nước dừa                           |")
    print("|[0] Bấm số 0 để thoát                  |")
    print('|_______________________________________|')

    chon = int(input('Chọn đồ uống: '))
    if chon == 1:
        print('Bạn đã chọn Cafe.')
    elif chon == 2:
        print('Bạn đã chọn Cam vắt.')
    elif chon == 3:
        print('Bạn đã chọn Nước ép cà rốt.')
    elif chon == 4:
        print('Bạn đã chọn Nước lọc.')
    elif chon == 5:
        print('Bạn đã chọn Nước dừa.')
    elif chon == 0:
        print('Đã thoát')
        break
    else:
        print('Chỉ chọn từ 1-5!')
    