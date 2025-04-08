students = {
    "123456": {"name": "Nguyễn Văn A", "score": 8},
    "234567": {"name": "Trần Thị B", "score": 9}
}

sbd = input("Nhập số báo danh: ")
if sbd in students:
    print(f"Họ tên: {students[sbd]['name']}, Điểm thi: {students[sbd]['score']}")
else:
    name = input("Nhập họ tên thí sinh: ")
    score = round(float(input("Nhập điểm thi: ")))
    students[sbd] = {"name": name, "score": score}
    print("Đã thêm thí sinh mới.")
