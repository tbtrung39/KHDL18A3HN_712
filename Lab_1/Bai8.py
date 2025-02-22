# Bài 8: 
ax, ay = map(float,input("Nhập tọa độ A(x,y):").split()) 
bx, by = map(float,input("Nhập tọa độ B(x,y):").split()) 
cx, cy = map(float,input("Nhập tọa độ C(x,y):").split()) 
gx = (ax + bx + cx)/3 
gy = (ay + by + cy)/3 
print(f"Trọng tâm của tam giác có tọa độ là G({gx:.2f},{gy:.2f})")