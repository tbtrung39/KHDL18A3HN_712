#Bai 1
thang=int(input("Nhập tháng(1->12)"))
if thang in [1,3,5,7,8,10,12]:
    print("Tháng",thang,"có 31 ngày")
elif thang in [4,6,9,11]:
    print("Tháng",thang,"có 30 ngày")
elif thang in [2]:
    print("Tháng",thang,"có 28 ngày")
else:
    print("Nhập sai vui lòng thử lại")
