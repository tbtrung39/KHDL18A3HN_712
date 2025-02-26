#Bai5
thang = int(input("Nhập tháng (1-12): "))
if thang<1 or thang>12:
    print("Nhập sai, vui lòng nhập lại!")
else:
    if thang==1:
        ten_thang = "January"
    elif thang==2:
        ten_thang = "February"
    elif thang==3:
        ten_thang = "March"
    elif thang==4:
        ten_thang = "April"
    elif thang==5:
        ten_thang = "May"
    elif thang==6:
        ten_thang = "June"
    elif thang==7:
        ten_thang = "July"
    elif thang==8:
        ten_thang = "August"
    elif thang==9:
        ten_thang = "September"
    elif thang==10:
        ten_thang = "October"
    elif thang==11:
        ten_thang = "November"
    elif thang==12:
        ten_thang = "December"
    print("Tháng", thang, "là:", ten_thang)
