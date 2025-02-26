#Bai11
thang=int(input("Nhập tháng:"))
if thang<1 or thang>12:
    print("Nhập sai, vui lòng nhập lại!")
else:
    if thang==1:
        ngay_cuoi=31
    elif thang==2:
        ngay_cuoi=28
    elif thang==3:
        ngay_cuoi=31
    elif thang==4:
        ngay_cuoi=30
    elif thang==5:
        ngay_cuoi=31
    elif thang==6:
        ngay_cuoi=30
    elif thang==7:
        ngay_cuoi=31
    elif thang==8:
        ngay_cuoi=31
    elif thang==9:
        ngay_cuoi=30
    elif thang==10:
        ngay_cuoi=31
    elif thang==11:
        ngay_cuoi=30
    else:
        ngay_cuoi=31
ngay_tiep_theo=1
thang_tiep_theo=thang+1
if thang==12:
    thang_tiep_theo=1
print("Ngày tiếp theo của ngày cuối cùng của tháng", thang, "là:", ngay_tiep_theo, "/", thang_tiep_theo)
