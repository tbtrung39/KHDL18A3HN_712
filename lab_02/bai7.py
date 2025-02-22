diem = float(input("Nhập điểm tổng kết: "))
if diem >= 0 and diem <= 3:
    print("Loại Kém")
elif diem == 4:
    print("Loại Yếu")
elif diem >= 5 and diem <= 6:
    print("Loại Trung Bình")
elif diem >= 7 and diem <= 8:
    print("Loại Khá")
elif diem >= 9 and diem <= 10:
    print("Loại Giỏi")
else:
    print("Điểm không hợp lệ!")
