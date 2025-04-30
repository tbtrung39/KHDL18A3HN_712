def find_max(a, b, c):
    # Hàm đệ quy để tìm số lớn nhất trong ba số
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Nhập 3 số từ bàn phím
num1 = float(input("Nhập số thứ nhất: "))
num2 = float(input("Nhập số thứ hai: "))
num3 = float(input("Nhập số thứ ba: "))

# Tìm số lớn nhất
max_number = find_max(num1, num2, num3)

print(f"Số lớn nhất trong ba số {num1}, {num2}, {num3} là: {max_number}")