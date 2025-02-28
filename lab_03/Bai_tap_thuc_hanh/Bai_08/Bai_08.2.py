n=int(input("Nhập số nguyên dương n:"))
if n <= 0:
    print("Không hợp lệ vui lòng nhập lại")
else:
    S2=(n+1)**2
    print(f"Tổng của 1+3+5+...+2*{n}+1 ={S2}")