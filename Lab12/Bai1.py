#Bai1:
import math
def ktra_tam_giac(a, b, c):
    return a + b > c and a + c > b and b + c > a
def nhap_canh():
    try:
        cac_canh = input("Nhap ba canh cua tam giac:").split()
        if len(cac_canh) != 3:
            raise ValueError("Phai nhap 3 gia tri.")
        a, b, c = map(float, cac_canh)
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Cac canh phai lon hon 0.")
        if not ktra_tam_giac(a, b, c):
            raise ValueError("Ba canh khong tao thanh mot tam giac.")
        return a, b, c
    except ValueError as e:
        print("Loi:", e)
        return None
def dtich_tam_giac(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))
while True:
    cac_canh=nhap_canh()
    if cac_canh:
        a,b,c=cac_canh
        dien_tich=dtich_tam_giac(a,b,c)
        print("Dien tich tam giac la:", dien_tich)
        break