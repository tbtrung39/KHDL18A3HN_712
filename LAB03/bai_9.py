n = int(input("nhập số nguyên dương:"))
if n <= 0:
    print("không hợp lệ vui lòng nhập lại")
else:
    S4 = 0
    for i in range(1,n+1):
        S4 += i**2
    S5 = 0
    for i in range(1,2*n+2,2):
        S5 += i**3
    S6 = 0
    for i in range(1,2*n+1,2):
        S6 += i**4
    print("tổng của biểu thức S4 là:",S4)
    print("tổng của biểu thức S5 là:",S5)
    print("tổng của biểu thức S6 là:",S6)