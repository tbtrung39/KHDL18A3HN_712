import os
print('\n CHƯƠNG TRÌNH GỌI ĐỒ UỐNG.')
while True:
    print('_________________________________________')
    print('|            Menu chọn đồ uống:          |')
    print('|[1] Cafe                                |')
    print('|[2] Cam vắt                             |')
    print('|[3] Nước ép cà rốt                      |')
    print('|[4] Nước lọc                            |')
    print('|[5] Nước dừa                            |')
    print('|________________________________________|')
    chon=int(input('Chọn nước muốn uống : '))
    if chon==1:
        print('Bạn chọn cà phê ')
    elif chon==2:
        print('Bạn chọn nước cam ')
    elif chon==3:
        print('Bạn chọn nước ép cà rốt ')
    elif chon==4:
        print('Bạn chọn nước lọc ')
    elif chon==5:
        print('Bạn chọn nước dừa ')
    else:
        print('không có nước bạn cần,vui lòng chọn nước khác')
        
        
        