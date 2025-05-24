import math

def la_tam_giac(a, b, c):
    return a + b > c and a + c > b and b + c > a

def tinh_dien_tich(a, b, c):
    nua_chu_vi = (a + b + c) / 2
    return math.sqrt(nua_chu_vi * (nua_chu_vi - a) * (nua_chu_vi - b) * (nua_chu_vi - c))

try:
    
    canh_a = float(input("Nhập cạnh a: "))
    canh_b = float(input("Nhập cạnh b: "))
    canh_c = float(input("Nhập cạnh c: "))

    
    if canh_a <= 0 or canh_b <= 0 or canh_c <= 0:
        raise ValueError("Các cạnh phải là số dương lớn hơn 0.")

    if not la_tam_giac(canh_a, canh_b, canh_c):
        raise ValueError("Ba cạnh không thỏa mãn điều kiện tạo thành tam giác.")

    danh_sach_canh = [canh_a, canh_b, canh_c]

    dien_tich = tinh_dien_tich(canh_a, canh_b, canh_c)
    print(f"Diện tích tam giác là: {dien_tich:.2f}")

except ValueError as loi:
    print(f"Lỗi: {loi}")

except Exception as loi_khac:
    print(f"Lỗi không xác định: {loi_khac}")
