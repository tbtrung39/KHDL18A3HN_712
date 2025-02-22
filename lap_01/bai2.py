a = int(input("nhap he so a: "))
b = int(input("nhap he so b: "))
c = int(input('nhap he so c: '))
if b**b + 4*a*c >0:
    print("phuong trinh co 2 nghiem")
elif b**b + 4*a*c < 0:
    print("phuong trinh vo nghiem")
elif b**b + 4*a*c == 0:
    print("phuong trinh co ngiem kep")
else :
    print("vui long nhap lai")
