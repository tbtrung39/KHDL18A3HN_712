#cau7:
Diem_TK = float(input("Nhập điểm tổng kết: "))
if 0.0 <= Diem_TK <= 3.0:
    print("Loại Kém")
elif Diem_TK == 4.0:
    print("Loại Yếu")
elif 5.0 <= Diem_TK <= 6.0:
    print("Loại Trung bình")
elif 7.0 <= Diem_TK <= 8.0:
    print("Loại Khá")
elif 9.0 <= Diem_TK <= 10.0:
    print("Loại Giỏi")
else:
    print("Điểm không hợp lệ!")