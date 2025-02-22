x1,y1=map(float,input("nhập toạ độ đỉnh A(x1,y1): ").split())
x2,y2=map(float,input("nhập toạ độ đỉnh B(x2,y2): ").split())
x3,y3=map(float,input("nhập toạ độ đỉnh C(x3,y3): ").split())
Gx=(x1+x2+x3)/3
Gy=(y1+y2+y3)/3
print(f"toạ độ trọng tâm:{Gx:.2f},{Gy:.2f}")