# Nhập số nguyên dương n
n = int(input("Nhập số nguyên dương n: "))
# Kiểm tra nếu n <= 0 thì yêu cầu nhập lại
while n <= 0:
    n = int(input("Vui lòng nhập số nguyên dương n: "))
# Biến lưu kết quả phân tích
result = []
# Dùng vòng lặp để phân tích n thành thừa số nguyên tố
for i in range(2, n + 1):
    while n % i == 0:  # Nếu i là ước của n
        result.append(i)
        n //= i  # Chia n cho i
# Xuất kết quả
print("Phân tích thừa số nguyên tố:", " × ".join(map(str, result)))