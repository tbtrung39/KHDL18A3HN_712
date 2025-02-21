x1, y1 = map(float, input("Nhap toa do dinh A (x1, y1): ").split())
x2, y2 = map(float, input("Nhap toa do dinh B (x2, y2): ").split())
x3, y3 = map(float, input("Nhap toa do dinh C (x3, y3): ").split())
Gx = (x1 + x2 + x3) / 3
Gy = (y1 + y2 + y3) / 3
print(f"Tọa độ trọng tâm G là: ({Gx:.2f}, {Gy:.2f})")
