import phuong_trinh

print("Giai pt bac nhat: ax + b = 0")
a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
print(phuong_trinh.giai_pt_bac_nhat(a, b))

print("\nGiai pt bac 2: ax^2 + bx + c = 0")
a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
c = float(input("Nhap c: "))
print(phuong_trinh.giai_pt_bac_hai(a, b, c))