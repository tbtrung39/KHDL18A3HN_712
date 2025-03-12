import math
while True:
    try:
        a = int(input("Nhập số nguyên thứ nhất: "))
        b = int(input("Nhập số nguyên thứ hai: "))
        if a == 0 or b == 0:
            print("Vui lòng nhập hai số nguyên khác 0!")
        else:
            break
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ!")
ucln = math.gcd(a, b)
bcnn = abs(a * b) // ucln 
print(f"Bội chung nhỏ nhất của {a} và {b} là: {bcnn}")