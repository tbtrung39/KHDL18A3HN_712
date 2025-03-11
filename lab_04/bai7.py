while True:
    a=int(input("Nhập số nguyên thứ nhất: "))
    b=int(input("Nhập số nguyên thứ hai: "))
    if a<0 or b<0:
        print("Lỗi đối biến. Vui lòng nhập số nguyên dương")
        continue
    if a==0 or b==0:
        print(f"Bội chung nhỏ nhất của {a} và {b} là 0")
        break
    x=a
    y=b
    while y!=0:
        yy=x%y
        x=y
        y=yy
        gtnn=x
    if a!=0 and b!=0:
        bcnn=abs(a*b)//gtnn
        print(f"Bội chung nhỏ nhất của {a} và {b} là {bcnn}")
        break
