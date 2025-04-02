tuples = []
while True:
    data = input("Nhập tuple (name, age, score) hoặc Enter để dừng: ")
    if not data:
        break
    name, age, score = data.split(",")
    tuples.append((name, int(age), int(score)))

tuples.sort(key=lambda x: (x[0], x[1], x[2]))
print(tuples)