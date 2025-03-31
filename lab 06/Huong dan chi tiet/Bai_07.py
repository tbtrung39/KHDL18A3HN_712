#Cách 1
import random

print("CHÒA MỪNG BẠN ĐẾN VỚI TRÒ CHƠI:ra Búa,Lá,Kéo!")
print("Bạn có 5 lượt chơi với computer")
print("Xin mời bạn lựa chọn ra:Búa/Lá/Kéo??")
print("Giá trị 0 đại diện cho ra búa")
print("Giá trị 1 đại diện cho ra kéo")
print("Giá trị 2 đại diện cho ra lá")
print("----------------------------")
thang=0
thua=0
hoa=0
for i in range(5):
    computer=random.randint(0,2)
    print("Ván thứ",i+1,"mời bạn chọn ra",end='')
    nguoi_choi=input("Búa(0),Kéo(1),Lá(2):")
    if computer==0:
        print("Computer đã chọn ra búa")
    elif computer==1:
        print('Computer đã chọn ra kéo')
    else:
        print("Computer đã chọn ra lá")
    if nguoi_choi not in ['0','1','2']:
        print("Sai luật mời nhập lại")
        continue

    nguoi_choi=int(nguoi_choi)
    if nguoi_choi==0:
        kq="Búa"
    elif nguoi_choi==1:
        kq="Kéo"
    else:
        kq="Lá"
    if computer==nguoi_choi:
        print("Ván này bạn đã ra",kq,"nên bên hòa Computer")
        hoa+=1
    elif (computer==0 and nguoi_choi==1) or (computer==1 and nguoi_choi==2) or (computer==1 and nguoi_choi==2) or (computer==2 and nguoi_choi==0):
        print("Bạn đã ra",kq,"nên bạn đã thua Computer!")
        thua += 1
    else:
        print("Bạn đã ra",kq,"nên bạn đã thắng Computer!")
        thang +=1
print("----------------------------------------------")
print('Tổng kết trò chơi')
print("Bạn đã thắng Computer",thang,"lần !")
print("Bạn đã hòa Computer",hoa,"lần !")
print("Bạn đã thua computer",thua,"lần !")