diem = float(input('Nhập điểm: '))
if 0 <= diem < 4:
    print('Loại Kém')
elif diem == 4:
    print('Loại Yếu')
elif 5 <= diem < 7:
    print('Loại Trung bình')
elif 7 <= diem < 9:
    print('Loại Khá')
elif 9 <= diem <= 10:
    print('Loại Giỏi')
else:
    print('Điểm không hợp lệ')