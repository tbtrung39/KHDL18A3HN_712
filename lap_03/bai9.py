# Nhập số nguyên dương n
n = int(input("Nhập số nguyên dương n: "))
# Kiểm tra nếu n <= 0 thì yêu cầu nhập lại
while n <= 0:
    n = int(input("Vui lòng nhập số nguyên dương n: "))
# Khởi tạo các biến tổng
S4 = 0  # Tổng bình phương các số tự nhiên
S5 = 0  # Tổng lập phương các số lẻ
S6 = 0  # Tổng lũy thừa 4 của các số chẵn
# Tính tổng S4: 1^2 + 2^2 + ... + n^2
for i in range(1, n + 1):
    S4 += i ** 2
# Tính tổng S5: 1^3 + 3^3 + 5^3 + ... + (2n+1)^3
for i in range(1, 2 * n + 2, 2):
    S5 += i ** 3
# Tính tổng S6: 2^4 + 4^4 + 6^4 + ... + (2n)^4
for i in range(2, 2 * n + 1, 2):
    S6 += i ** 4
# Xuất kết quả
print(f"S4 = 1² + 2² + ... + {n}² = {S4}")
print(f"S5 = 1³ + 3³ + ... + (2n+1)³ = {S5}")
print(f"S6 = 2⁴ + 4⁴ + ... + (2n)⁴ = {S6}")