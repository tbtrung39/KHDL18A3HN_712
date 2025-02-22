#cau8:
xa, ya = map(float,input('Nhập tọa độ đỉnh 1 của tam giác:').split())
xb, yb = map(float,input('Nhập tọa độ đỉnh 2 của tam giác:').split())
xc, yc = map(float,input('Nhập tọa độ đỉnh 3 của tam giác:').split())
xg = (xa + xb + xc)/3
yg = (ya + yb + yc)/3
print(f"Tọa độ trọng tâm G của tam giác là: {xg:.2f}, {yg:.2f}")
