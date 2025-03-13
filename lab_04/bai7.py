a = int(input("Nhập số nguyên đầu tiên: "))
b = int(input("Nhập số nguyên thứ hai: "))
if a == 0:
    print("Hãy nhập a khác số 0")
elif b == 0:
    print("Hãy nhập b khác số 0")
else:
    x, y = a, b
    while y != 0:
        x, y = y, x % y  
    ucln = abs(x)  
    bcnn = abs(a * b) // ucln
    print("Bội chung nhỏ nhất của", a, "và", b, "là:", bcnn)