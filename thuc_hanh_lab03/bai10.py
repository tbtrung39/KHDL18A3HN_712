n = int(input("Nhap so nguyen duong n là:"))
kiem_tra = 1
if n<2:
    kiem_tra = 0
elif n == 2:
    kiem_tra = 1
else:
    for i in range(3, n):
        if n % i == 0:
            kiem_tra = 0 
            break
        else:
            kiem_tra = 1
if kiem_tra == 1:
    print("Đây là số nguyên tố")
else:
    print("Đây không phải là số nguyên tố")