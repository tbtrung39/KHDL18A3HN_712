so_du=0
while True:
    giao_dich=input("nhap giao dich D <số tiền> hoac W <số tiền> ('x' de ket thuc)")
    if giao_dich.lower=='x':
        break
    a=giao_dich.split()
    if len(a)==2:
        b,c=a
        c=int(c)
        if b=='D':
            so_du+=c
        elif b=='W':
            so_du-=c
        else:
            print("giao dich khong hop le.")
    else:
        print("dinh dang giao dich khong dung")
print(f"so du tai khoan sau khi thuc hien cac giao dich la: {so_du}")