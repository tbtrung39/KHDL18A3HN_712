def power(a, n):
    # Hàm đệ quy để tính a^n
    if n == 0:
        return 1  # Bất kỳ số nào mũ 0 đều bằng 1
    elif n < 0:
        return 1 / power(a, -n)  # Xử lý trường hợp mũ âm
    else:
        return a * power(a, n - 1)  # Đệ quy

# Nhập số a và n từ bàn phím
a = float(input("Nhập số a: "))
n = int(input("Nhập số n: "))

# Tính lũy thừa
result = power(a, n)

print(f"{a} ^ {n} = {result}")