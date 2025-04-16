#Bai9
def tinh_cong_tru_nhan_chia(a, b):
    if b != 0:
        return a + b, a - b, a * b, a / b
    else:
        print("Khong chia duoc cho 0!")
a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
tong, hieu, tich, thuong = tinh_cong_tru_nhan_chia(a, b)
print("Phep cong:", tong)
print("Phep tru:", hieu)
print("Phep nhan:", tich)
print("Phep chia:", thuong)