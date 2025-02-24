a, b, c = map(float, input("Nhap he so a, b, c: ").split())
delta = (b**2) - (4*a*c)
if delta < 0:
    print("Phuong trinh da cho vo nghiem")
elif delta == 0:
    print("Phuong trinh da cho co nghiem kep: ")
    print("x1 = x2 =", -b/(2*a))
else:
    print("Phuong trinh da cho co 2 nghiem phan biet:")
    x1 = (-b + (delta**0.5)) / (2*a)
    x2 = (-b - (delta**0.5)) / (2*a)
    print("x1 =", x1)
    print("x2 =", x2)