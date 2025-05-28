import math
try:
    a = float(input("Nhập cạnh a: "))
    b = float(input("Nhập cạnh b: "))
    c = float(input("Nhập cạnh c: "))
    sides = [a, b, c]
    if a <= 0 or b <= 0 or c <= 0:
        print("Lỗi: Các cạnh phải là số dương lớn hơn 0.")
    elif a + b <= c or a + c <= b or b + c <= a:
        print("Lỗi: Ba cạnh không thỏa mãn điều kiện tạo thành tam giác.")
    else:
        p = (a + b + c) / 2
        area = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print("Danh sách cạnh:", sides)
        print("Diện tích tam giác là:", area)
except ValueError:
    print("Lỗi: Bạn phải nhập số cho cả ba cạnh.")
