# cach 1
n = int(input("Nhap so nguyen n: "))
binary_str = bin(n)[2:]
print(f"So nhi phan tuong ung: {binary_str}")
# cách 2
n = int(input("Nhap so nguyen n: "))
if n == 0:
    binary_str = "0"
else:
    binary_str = ""
    while n > 0:
        binary_str = str(n % 2) + binary_str  
        n //= 2  
print(f"So nhi phan tuong ung: {binary_str}")
