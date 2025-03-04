score = float(input("Nhập điểm trung bình của học sinh: "))
if 0 <= score <= 3.0:
    print("Loại Kém")
elif score == 4.0:
    print("Loại Yếu")
elif 5.0 <= score <= 6.0:
    print("Loại Trung bình")
elif 7.0 <= score <= 8.0:
    print("Loại Khá")
elif 9.0 <= score <= 10.0:
    print("Loại Giỏi")
else:
    print("Điểm không hợp lệ.")