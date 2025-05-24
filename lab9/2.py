def gcd(a, b):
    # Hàm đệ quy để tính UCLN của hai số a và b
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def gcd_of_list(numbers):
    # Hàm tính UCLN của danh sách các số
    if len(numbers) == 1:
        return numbers[0]
    else:
        return gcd(numbers[0], gcd_of_list(numbers[1:]))

# Nhập số lượng n
n = int(input("Nhập số lượng số cần tính UCLN: "))

# Nhập n số từ bàn phím
numbers = []
for i in range(n):
    num = int(input(f"Nhập số thứ {i + 1}: "))
    numbers.append(num)

# Tính UCLN
result = gcd_of_list(numbers)

print(f"Ước chung lớn nhất của {numbers} là: {result}")