import math

def tam_giac(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Cạnh tam giac phai lon hon 0.")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Ba canh khong thoa man dieu kien tam giac.")
    p = (a + b + c)/ 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

try:
    a = float(input("Nhập cạnh a: "))
    b = float(input("Nhập cạnh b: "))
    c = float(input("Nhập cạnh c: "))
    dientich = tam_giac(a, b, c)
    print(f"Dien tich tam giac la: {dientich:.2f}")
except ValueError as e:
    print("Lỗi:", e)
except Exception:
    print("Loi: Du lieu nhap khong hop le.")