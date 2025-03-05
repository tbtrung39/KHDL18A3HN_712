n = int(input("Nhập số nguyên n: "))
S = 0
for i in range(1, n + 1):
    S += i**3
print(f"Tổng bậc 3 của {n} số nguyên đầu tiên là: {S}")
