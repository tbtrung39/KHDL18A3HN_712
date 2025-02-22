x_A = float(input('Nhập hoành độ điểm A: '))
y_A = float(input('Nhập tung độ điểm A: '))
x_B = float(input('Nhập hoành độ điểm B: '))
y_B = float(input('Nhập tung độ điểm B: '))
x_C = float(input('Nhập hoành độ điểm C: '))
y_C = float(input('Nhập tung độ điểm C: '))
G_x = (x_A + x_B + x_C) / 3
G_y = (y_A + y_B + y_C) / 3
print(f'Tọa độ trọng tâm của tam giác là: ({G_x:.2f}, {G_y:.2f})')
