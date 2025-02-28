n=int(input("Nhập số nguyên dương n:"))
if n <= 0:
    print("Số không hợp lệ vui lòng nhập lại")
S4=0
for i in range(1,n+1):
    S4 += i**2
print(f"Tổng của 1**2 +2**2+3**2+...+{n}**2 ={S4}")