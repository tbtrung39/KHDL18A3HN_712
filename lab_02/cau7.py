diem = float(input("Nhập điểm tổng kết: "))
if diem < 3.0:
    print("Loại Kém")
elif 3.0 <= diem < 4.0:
    print("Loại Yếu")
elif 5.0 <= diem < 6.0:
    print("Loại Trung Bình")
elif 7.0 <= diem < 8.0:
    print("Loại Khá")
else:
    print("Loại Giỏi")