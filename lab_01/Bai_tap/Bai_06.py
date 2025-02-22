#Bài 6
U=220
I=27
Gia_dien=7000
time=float(input("Nhập thời gian sử dụng bóng đèn"))
P=U*I
Tieu_thu=P*time
kWh=Tieu_thu/(3.6 * 10**6)
tien_dien=kWh*Gia_dien
tien_dien=round(tien_dien,2)
print(f"Tiền điện phải trả:{tien_dien}đồng")#Bài 8
xA,yA=map(float,input("Nhập tọa độ điểm A(xA yA):").split())
xB,yB=map(float,input("Nhập tọa độ của điểm B(xB yB):").split())
xC,yC=map(float,input("Nhập toạ độ điểm C(xC yC):").split())
xG=(xA+xB+xC)/3
yG=(yA+yB+yC)/3
xG=round(xG,2)
yG=round(yG,2)
print(f"Trọng tâm của tam giác là:({xG},{yG})")