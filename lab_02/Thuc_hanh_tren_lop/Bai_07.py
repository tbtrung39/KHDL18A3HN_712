# bài 7
Diem_TK = float(input("Nhập điểm tổng kết: "))
if 0.0 <= Diem_TK <= 3.0:
    print("XếpXếp loại Kém")
elif Diem_TK == 4.0:
    print("Xếp loại Yếu")
elif 5.0 <= Diem_TK <= 6.0:
    print(" Xếp loại Trung bình")
elif 7.0 <= Diem_TK <= 8.0:
    print(" Xếp loại Khá")
elif 9.0 <= Diem_TK <= 10.0:
    print("Xếp loại Giỏi")
else:
    print("Nhập sai vui lòng thử lại")
