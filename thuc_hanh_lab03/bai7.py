n = int(input("Nhập số nguyên n là: "))
S = 0
for i in range(1, n+1):
    S += 1/i
S = round(S, 3)
print("Tổng nghịch đảo của n số nguyên đầu tiên là: ",S)