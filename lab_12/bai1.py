# bai 1
import math

def nhap_canh_tam_giac():
    try:
        canh = input("Nhap 3 canh tam giac tu ban phim: ").split()
        if len(canh) != 3:
            raise ValueError("hay nhap ba gia tri")
        a, b, c = map(float, canh)
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("nhap canh tam giac lon hon 0.")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Ba canh khong thoa man dieu kien ton tai tam giac.")
        return a, b, c

    except ValueError as ve:
        print("Loi:", ve)
        return None

def tinh_dien_tich_tam_giac(a, b, c):
    p = (a + b + c) / 2
    dien_tich = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return dien_tich

ds_canh = nhap_canh_tam_giac()
if ds_canh:
    a, b, c = ds_canh
    s = tinh_dien_tich_tam_giac(a, b, c)
    print(f"Dien tich tam giac la: {s:.2f}")
