try:
    a = float(input("Nhập cạnh a: "))
    b = float(input("Nhập cạnh b: "))
    c = float(input("Nhập cạnh c: "))

    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Cạnh không được âm hoặc bằng 0.")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Ba cạnh không tạo thành tam giác.")

    print("Đây là tam giác hợp lệ.")

except ValueError as e:
    print(f"Lỗi: {e}")