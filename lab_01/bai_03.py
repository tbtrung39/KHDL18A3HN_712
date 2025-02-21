r = float(input("Nhap ban kinh: "))
h = float(input("Nhap chieu cao: "))
pi = 3.14
s_xq = 2*pi*r*h
s_tp = 2*pi*r*(r+h)
V = pi*r**2*h
print(f"Dien tich xung quanh: {s_xq:.2f}")
print(f"Dien tich toan phan: {s_tp:.2f}")
print(f"The tich: {V:.2f}")