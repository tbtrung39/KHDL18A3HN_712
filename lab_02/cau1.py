thang = int(input("Nhập tháng (1-12): "))
if thang==[1,3,5,7,8,10,12]:
    print("tháng",thang,"có 31 ngày")
elif thang==[4,6,9,11]:
    print("tháng",thang,"có 30 ngày")
elif thang==2:
    print("tháng 2 có 28 ngày")
else:
    print("Tháng không hợp lệ!")