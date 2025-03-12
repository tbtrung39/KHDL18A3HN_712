n1 = int(input("nhập số thứ nhất:"))
n2 = int(input("nhập số thứ hai:"))
a = n1
b = n2
while n2 != 0:
    n1,n2 = n2,n1 % n2
    ucln = n1
    bcnn = (a*b)//ucln
    print(f"{bcnn}")
