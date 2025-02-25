ten_thang = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

while True:
    so_thang = input("Nhập số tháng (1->12): ")
    if so_thang.isdigit():
        so_thang = int(so_thang)
        if 1 <= so_thang <= 12:
            print("Tháng bạn nhập là:", ten_thang[so_thang - 1])
            break
    print("Giá trị không hợp lệ, vui lòng nhập lại!")