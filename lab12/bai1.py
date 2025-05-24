import math

def tinh_dien_tich_tam_giac(a, b, c):
    try:
        a, b, c = float(a), float(b), float(c)
        if a <= 0 or b <= 0 or c <= 0:
            return "do dai cac canh phai lon hon 0"
        if a + b <= c or b + c <= a or a + c <= b:
            return "khong thoa man dieu kien ton tai tam giac"
        p = (a + b + c) / 2
        dien_tich = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return dien_tich
    except ValueError:
        return "nhap sai yeu cau"

a = input("nhap canh a: ")
b = input("nhap canh b: ")
c = input("nhap canh c: ")
list_canh = [a, b, c]
print("list cac canh:", list_canh)
print("dien tich tam giac:", tinh_dien_tich_tam_giac(a, b, c))