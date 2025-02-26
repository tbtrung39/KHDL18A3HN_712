#Bai1
thang=int(input("Nhập tháng(1-12): "))
if thang<1 or thang>12:
    print("Nhập sai, vui lòng nhập lại!")
else:
    if thang in(1,3,5,7,8,10,12):
        ngay=31
    elif thang in(4,6,9,11):
        ngay=30
    else:
        ngay=28
    print("Tháng", thang, "có", ngay, "ngày.")