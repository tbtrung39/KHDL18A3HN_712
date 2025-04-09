students = {}
n = int(input("Nhập số sinh viên: "))

for _ in range(n):
    msv = input("Mã sinh viên (6 số): ")
    name = input("Tên sinh viên: ")
    score = round(float(input("Điểm số (0-10): ")))
    students[msv] = {"name": name, "score": score}

# Sắp xếp theo điểm giảm dần
sorted_students = sorted(students.items(), key=lambda x: x[1]['score'], reverse=True)

print("Danh sách sinh viên theo điểm giảm dần:")
for msv, info in sorted_students:
    print(f"Mã SV: {msv}, Tên: {info['name']}, Điểm: {info['score']}")