n = int(input("Nhập số nguyên dương n: "))
if n <= 0:
    print("Số không hợp lệ vui lòng nhập lại")  
S6 = sum((2 * i) ** 4 for i in range(1, n + 1))
print(f"Tổng S6 = 2**4 + 4**4+6**4 + ... + (2*{n})**4 là: {S6}")