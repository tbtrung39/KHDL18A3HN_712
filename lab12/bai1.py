import math

def tinh_dien_tich_tam_giac(a, b, c):
    try:
        a, b, c = float(a), float(b), float(c)
        if a <= 0 or b <= 0 or c <= 0:
            return "Độ dài các cạnh phải lớn hơn 0"
        if a + b <= c or b + c <= a or a + c <= b:
            return "Không thỏa mãn điều kiện tồn tại tam giác"
        p = (a + b + c) / 2
        dien_tich = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return dien_tich
    except ValueError:
        return "Đầu vào phải là số"

a = input("Nhập cạnh a: ")
b = input("Nhập cạnh b: ")
c = input("Nhập cạnh c: ")
list_canh = [a, b, c]
print("List các cạnh:", list_canh)
print("Diện tích tam giác:", tinh_dien_tich_tam_giac(a, b, c))