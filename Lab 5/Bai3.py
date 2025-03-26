#Bai3
n = int(input("Nhập số tự nhiên n: "))
binary = ' '
if n == 0:
    binary = '0'
else:
    while n > 0:
        binary = str(n % 2) + binary 
        n = n // 2 
print("Chuỗi nhị phân:", binary)