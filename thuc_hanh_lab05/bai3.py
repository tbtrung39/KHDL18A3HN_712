n = int(input("Nhập số tự nhiên n là: "))
binary = ""  
while n > 0:
    binary = str(n % 2) + binary  
    n //= 2  
if binary == "":  
    binary = "0"
print("Chuỗi nhị phân:", binary)