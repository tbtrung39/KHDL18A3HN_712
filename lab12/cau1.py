import math

def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def triangle_area(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

try:
    a = float(input("Nhập cạnh a: "))
    b = float(input("Nhập cạnh b: "))
    c = float(input("Nhập cạnh c: "))

    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Cạnh phải là số dương lớn hơn 0.")
    
    if not is_triangle(a, b, c):
        raise ValueError("Ba cạnh không tạo thành một tam giác hợp lệ.")
    
    tamgiac = [a, b, c]
    dientich = triangle_area(a, b, c)
    print(f"Tam giác {tamgiac} có diện tích: {dientich:.2f}")

except ValueError as ve:
    print("Lỗi:", ve)
except Exception:
    print("Đã xảy ra lỗi không xác định.")
