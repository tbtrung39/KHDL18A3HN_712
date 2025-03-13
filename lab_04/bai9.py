while True:
    try:
        num = int(input("Nhập một số nguyên dương: "))
        if num < 0:
            print("Vui lòng nhập số không âm!")
        else:
            break
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ!")
tong = 0
temp = num 
while temp > 0:
    tong += temp % 10
    temp //= 10 
print(f"Tổng các chữ số của {num} là: {tong}")