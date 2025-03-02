n = int(input("Nhập n: "))
while n <= 0:
    n = int(input("Vui lòng nhập n > 0: "))
S = 0
for i in range(1, n+1):
    S += 1/i
print("Tổng nghịch đảo:", S)
