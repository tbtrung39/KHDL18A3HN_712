import math

def S_tam_giac(a, b, c):
    try:
        a, b, c = float(a), float(b), float(c)
        if a <= 0 or b <= 0 or c <= 0:
            return "Do dai cac canh phai lon hon 0"
        if a + b <= c or b + c <= a or a + c <= b:
            return "Khong thoa man dieu kien ton tai tam giac"
        p = (a + b + c) / 2
        dien_tich = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return dien_tich
    except ValueError:
        return "Nhap sai yeu cau"

a = input("Nhap canh a: ")
b = input("Nhap canh b: ")
c = input("Nhap canh c: ")
list_canh = [a, b, c]
print("Danh sach cac canh:", list_canh)
print("Dien tich tam giac:", S_tam_giac(a, b, c))