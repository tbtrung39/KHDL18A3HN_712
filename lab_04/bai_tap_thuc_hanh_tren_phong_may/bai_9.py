while True:
    n = input("Nhập một số: ")
    i = 0
    while n[i:] and (n[i] == "-" or "0" <= n[i] <= "9"):  
        i += 1
    if not n[i:] and n != "-":  
        n = int(n)
        break
    
n = abs(n)  
tong = 0

while n > 0:
    tong += n % 10  
    n //= 10  

print("Tổng các chữ số là:", tong)
