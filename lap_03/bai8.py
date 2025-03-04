# Nhập số nguyên dương n
n = int(input("Nhập số nguyên dương n: "))
# Kiểm tra nếu n <= 0 thì yêu cầu nhập lại
while n <= 0:
    n = int(input("Vui lòng nhập số nguyên dương n: "))
# Tính tổng S1 = 1 + 2 + 3 + ... + n
S1 = 0
for i in range(1, n + 1):
    S1 += i
# Tính tổng S2 = 1 + 3 + 5 + ... + (2n+1)
S2 = 0
for i in range(1, 2 * n + 2, 2):  # Dãy số lẻ: 1, 3, 5, ..., (2n+1)
    S2 += i
# Tính tổng S3 = 2