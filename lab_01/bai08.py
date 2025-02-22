# Nhập tọa độ của 3 đỉnh A, B, C
xA = float(input("Nhập tọa độ x của đỉnh A: "))
yA = float(input("Nhập tọa độ y của đỉnh A: "))

xB = float(input("Nhập tọa độ x của đỉnh B: "))
yB = float(input("Nhập tọa độ y của đỉnh B: "))

xC = float(input("Nhập tọa độ x của đỉnh C: "))
yC = float(input("Nhập tọa độ y của đỉnh C: "))

# Tính tọa độ trọng tâm (G)
xG = (xA + xB + xC)/3
yG = (yA + yB + yC)/3

xG = round(xG, 2)
yG = round(yG, 2)

# Hiển thị kết quả
print(f"Tọa độ trọng tâm G của tam giác là: (xG, yG) = ({xG}, {yG})")