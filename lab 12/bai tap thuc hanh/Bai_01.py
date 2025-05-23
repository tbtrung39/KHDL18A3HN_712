import math

def nhap_canh(ten_canh):
    while True:
        try:
            canh = float(input(f"Nhập cạnh {ten_canh}: "))
            if canh <= 0:
                raise ValueError("Cạnh phải lớn hơn 0.")
            return canh
        except ValueError as e:
            print("Lỗi:", e)

def la_tam_giac(a, b, c):
    return a + b > c and a + c > b and b + c > a

try:
    print("=== Nhập 3 cạnh của tam giác ===")
    a = nhap_canh("a")
    b = nhap_canh("b")
    c = nhap_canh("c")

    if not la_tam_giac(a, b, c):
        raise Exception("Ba cạnh không thỏa mãn điều kiện !")
    p = (a + b + c) / 2
    dientich = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(f"Diện tích tam giác là: {dientich:.2f}")

except Exception as e:
    print("Lỗi:", e)
