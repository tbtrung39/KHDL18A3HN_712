so_du=0
while True:
    giao_dich=input("nhập giao dịch D <số tiền> hoặc W <số tiền> ('x' để kết thúc)")
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
            print("giao dịch không hợp lệ.")
    else:
        print("định dạng giao dịch không đúng")
print(f"số dư tài khoản sau khi thực hiện các giao dịch là: {so_du}")