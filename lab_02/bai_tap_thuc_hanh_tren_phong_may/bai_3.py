thu = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
ngay = input("Nhập số thứ trong tuần (1->7): ")
if ngay.isdigit():
    ngay = int(ngay)
    if 1 <= ngay <= 7:
        print("Thứ bạn nhập là:", thu[ngay - 1])
    else:
        print("Giá trị không hợp lệ!")
else:
    print("Giá trị không hợp lệ!")