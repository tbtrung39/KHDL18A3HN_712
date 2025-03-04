# Nhập số nguyên dương n
n = int(input("Nhập số nguyên dương n: "))
# Kiểm tra nếu n < 1 thì yêu cầu nhập lại
while n < 1:
    n = int(input("Vui lòng nhập số nguyên dương n: "))
# Khởi tạo biến tổng
tong = 0.0
# Tính tổng nghịch đảo
for i in range(1, n + 1):
    tong += 1 / i
# Xuất kết quả
print(f"Tổng nghịch đảo của {n} số nguyên đầu tiên là: {tong}")