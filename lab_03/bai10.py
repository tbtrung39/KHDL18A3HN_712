n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    n = int(input("Vui lòng nhập số nguyên dương n: "))
result = []
for i in range(2, n + 1):
    while n % i == 0:  
        result.append(i)
        n //= i 
print("Phân tích thừa số nguyên tố:", " × ".join(map(str, result)))
