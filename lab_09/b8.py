import math

# Tính tổng S = ∑(1/i!) từ i=1 đến n
def calculate_sum_factorial(n):
    S = 0
    for i in range(1, n + 1):
        S += 1 / math.factorial(i)
    return S

# Tính tổng S = √(3*i + S) từ i=1 đến n
def calculate_sum_sqrt_c(n):
    S = 0
    for i in range(1, n + 1):
        S = math.sqrt(3 * i + S)
    return S

# Tính tổng S = √(n + 2 - i + S) từ i=1 đến n+1
def calculate_sum_sqrt_d(n):
    S = 0
    for i in range(1, n + 2):  # từ 1 đến n+1
        S = math.sqrt(n + 2 - i + S)
    return S

# Nhập giá trị n và kiểm tra tính hợp lệ
while True:
    try:
        n = int(input("Nhập giá trị n (số tự nhiên): "))
        if n < 1:
            raise ValueError("Vui lòng nhập một số tự nhiên lớn hơn 0.")
        break
    except ValueError as e:
        print(e)

# Tính và in kết quả
print(f"Câu a và b: S = {calculate_sum_factorial(n):.6f}")
print(f"Câu c: S = {calculate_sum_sqrt_c(n):.6f}")
print(f"Câu d: S = {calculate_sum_sqrt_d(n):.6f}")