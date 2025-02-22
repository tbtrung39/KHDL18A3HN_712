x_A, y_A = map(float, input('Nhập tọa độ điểm A: ').split())
x_B, y_B = map(float, input('Nhập hoành độ điểm B: ').split())
x_C, y_C = map(float, input('Nhập hoành độ điểm C: ').split())
G_x = (x_A + x_B + x_C) / 3
G_y = (y_A + y_B + y_C) / 3
print(f'Tọa độ trọng tâm của tam giác là: ({G_x:.2f}, {G_y:.2f})')