students = {}
n = int(input("Nhập số sinh viên: "))

for _ in range(n):
    msv = input("Mã sinh viên (6 số): ")
    name = input("Tên sinh viên: ")
    score = round(float(input("Điểm số (0-10): ")))
    students[msv] = {"name": name, "score": score}

# Sắp xếp theo điểm giảm dần
sorted_students = sorted(students.items(), key=lambda x: x[1]['score'], reverse=True)

print("Danh sach sinh vien theo diem giam dan:")
for msv, info in sorted_students:
    print(f"Ma SV: {msv}, Ten: {info['name']}, Điem: {info['score']}")