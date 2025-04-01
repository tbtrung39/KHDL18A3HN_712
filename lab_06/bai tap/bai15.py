data = []
while True:
    entry = input("Nhập tuple (name, age, score) hoặc bấm Enter để dừng: ")
    if not entry:
        break
    name, age, score = entry.split(",")
    data.append((name.strip(), int(age.strip()), int(score.strip())))

data.sort(key=lambda x: (x[0], x[1], x[2]))

print("\nDanh sách sau khi sắp xếp:")
for item in data:
    print(item)
