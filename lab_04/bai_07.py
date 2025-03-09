n = int(input("Nhap n: "))
m = int(input("Nhap m: "))
a, b = n, m
while n != 0:
    m, n = n, m % n
    
bcnn = a * b // m
print(f"BCNN của {a} và {b} là {bcnn}")
