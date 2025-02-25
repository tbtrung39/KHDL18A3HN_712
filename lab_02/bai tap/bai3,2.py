day = int(input("Nhập vào thứ (1-7): "))
if 1 <= day <= 7:
    print("Thứ không hợp lệ, vui lòng nhập lại.")

if day == 1:
    print("Sunday")
elif day == 2:
    print("Monday")
elif day == 3:
    print("Tuesday")
elif day == 4:
    print("Wednesday")
elif day == 5:
    print("Thursday")
elif day == 6:
    print("Friday")
else:
    print("Saturday")
