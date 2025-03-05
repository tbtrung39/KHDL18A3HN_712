n = int(input("nhập số nguyên dương:"))
if n <= 0:
    print("không hợp lệ vui lòng nhập lại")
else:
    S = 0
    for i in range(1,n+1):
        S += 1 / i
    print(f"tống số nghịch đảo {n} só nguyên đầu tiên là: {S} ")

