thu = int(input('Nhập vào thứ trong tuần (1->7): '))
if thu == 1:
    print(f'{thu}: Sunday')
elif thu == 2:
    print(f'{thu}: Monday')
elif thu == 3:
    print(f'{thu}: Tuesday')
elif thu == 4:
    print(f'{thu}: Wednesday')
elif thu == 5:
    print(f'{thu}: Thursday')
elif thu == 6:
    print(f'{thu}: Friday')
elif thu == 7:
    print(f'{thu}: Saturday')
else:
    print('Thứ không hợp lệ. Vui lòng nhập lại!')
