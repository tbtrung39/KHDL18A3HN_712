n=int(input("Nhập số nguyên dương n:"))
if n <= 0:
    print("Số không hợp lệ vui lòng nhập lại")
else:
    S1=n*(n+1)/2
    print(f"Tổng của biểu thức 1+2+3+...+ {n} ={S1}")