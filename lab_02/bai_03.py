ten_thu = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
thu = int(input("Nhập thứ trong tuần (1-7): "))

if 1 <= thu <= 7:
    print("Thứ bạn đã nhập là:", ten_thu[thu])
else:
    print("Thứ không hợp lệ, vui lòng nhập lại!")