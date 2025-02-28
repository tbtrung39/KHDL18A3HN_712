n = int(input("Nhập số nguyên dương n: "))
if n <= 0:
    print("Vui lòng nhập một số nguyên dương!")
else:
    Tong = (n * (n + 1) // 2) ** 2
    print(f"Tổng bậc 3 của {n} số nguyên đầu tiên là: {Tong}")
