n=int(input("Nhập số nguyên dương n:"))
if n <= 0:
    print("Số không hợp lệ vui lòng nhập lại")
else:
    S3=n*(n+1)
    print(f"Tổng của 2+4+6+...+2*{n}={S3}")