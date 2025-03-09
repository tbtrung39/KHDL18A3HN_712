n = int(input("Nhap số nguyên thứ nhất n là: "))
m = int(input("Nhap số nguyên thứ hai m là: "))
a, b = n, m
while n != 0:
    m, n = n, m % n
     
bcnn = a * b // m
print(f"BCNN của {a} và {b} là {bcnn}")