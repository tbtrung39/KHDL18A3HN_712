#Bai7
diem_tb= float(input("Nhập điểm trung bình : "))
if diem_tb<0 or diem_tb>10:
    print("Nhập sai, vui lòng nhập lại!")
else:
    if diem_tb>=9.0 and diem_tb<=10.0:
        xep_loai = "Giỏi"
    elif diem_tb>=7.0 and diem_tb<9.0:
        xep_loai = "Khá"
    elif diem_tb>=5.0 and diem_tb<7.0:
        xep_loai = "Trung Bình"
    elif diem_tb>=4.0 and diem_tb<5.0:
        xep_loai = "Yếu"
    else:
        xep_loai = "Kém"
    print("Điểm trung bình là", diem_tb, "và xếp loại", xep_loai)
