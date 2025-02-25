diem = input("Nhập điểm của sinh viên (A, B, C, D, E, F): ").upper()
if diem == "A":
    print("Sinh viên xuất sắc.")
elif diem == "B":
    print("Sinh viên loại giỏi.")
elif diem == "C":
    print("Sinh viên loại khá.")
elif diem == "D":
    print("Sinh viên loại trung bình.")
elif diem == "E":
    print("Sinh viên loại yếu.")
elif diem == "F":
    print("Sinh viên xếp loại kém.")
else:
    print("Điểm không hợp lệ. Vui lòng nhập A, B, C, D, E hoặc F.")
