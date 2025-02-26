#Bai3
thu=int(input("Nhập vào thứ (1-7): "))
if thu<1 or thu>7:
    print("Nhập sai, vui lòng nhập lại!")
else:
    if thu==1:
        ten_thu="Sunday"
    elif thu==2:
        ten_thu="Monday"
    elif thu==3:
        ten_thu="Tuesday"
    elif thu==4:
        ten_thu="Wednesday"
    elif thu==5:
        ten_thu="Thursday"
    elif thu==6:
        ten_thu="Friday"
    elif thu==7:
        ten_thu="Saturday"
    print("Thứ", thu, "là", ten_thu)
