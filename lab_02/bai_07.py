diem_tk = float(input("Nhập điểm tổng kết: "))

if 0.0 <= diem_tk <= 3.0:
    print("Loại Kém")
elif diem_tk == 4.0:
    print("Loại Yếu")
elif 5.0 <= diem_tk <= 6.0:
    print("Loại Trung Bình")
elif 7.0 <= diem_tk <= 8.0:
    print("Loại Khá")
elif 9.0 <= diem_tk <= 10.0:
    print("Loại Giỏi")
else:
    print("Điểm không hợp lệ!")
