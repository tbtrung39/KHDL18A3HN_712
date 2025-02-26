ten_thang = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
thang = int(input("Nhập vào tháng (1-12): "))

if 1 <= thang <= 12:
    print("Tháng bạn đã nhập là: ",ten_thang[thang])
else:
    print("Tháng không hợp lệ, vui lòng nhập lại!")
