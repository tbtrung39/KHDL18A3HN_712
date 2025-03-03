#tọa độ AA
x1 = float(input("Nhập hoành độ x1 của đỉnh A: "))
y1 = float(input("Nhập tung độ y1 của đỉnh A: "))
#Tọa độ BB
x2 = float(input("Nhập hoành độ x2 của đỉnh B: "))
y2 = float(input("Nhập tung độ y2 của đỉnh B: "))
#tọa độ C
x3 = float(input("Nhập hoành độ x3 của đỉnh C: "))
y3 = float(input("Nhập tung độ y3 của đỉnh C: "))
#tínhtính
xG = (x1 + x2 + x3) / 3
yG = (y1 + y2 + y3) / 3
print(f"Tọa độ trọng tâm của tam giác: ({xG:.2f}, {yG:.2f})")
