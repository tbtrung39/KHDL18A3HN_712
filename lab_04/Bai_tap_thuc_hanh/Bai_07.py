so_thu_nhat=int(input("Nhập số nguyên thứ nhất:"))
so_thu_hai=int(input("Nhập số nguyên thứ hai:"))
a=so_thu_nhat
b=so_thu_hai
while b!=0:
    a,b=b,a%b
ucln=a
bcnn=abs(so_thu_nhat*so_thu_hai)//ucln
print("Bội chung nhỏ nhất của",so_thu_nhat,"và",so_thu_hai,"là",bcnn)