import phuong_trinh
print("Giai pt bac nhat: ax + b = 0")
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
print(phuong_trinh.Pt_bac_nhat(a, b))

print("\nGiai phuong trinh bac 2: ax^2 + bx + c = 0")
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
print(phuong_trinh.Pt_bac_hai(a, b, c))