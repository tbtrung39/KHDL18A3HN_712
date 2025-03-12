# a) Tính tổng S1 = 1^2 + 2^2 + 3^2 + ... + n1^2
n1 = int(input('Nhập n1: '))
while n1 <= 0:
    n1 = int(input('Vui lòng nhập lại n1 (n1 > 0): '))
S1 = 0
i = 1
while i <= n1:
    S1 += i ** 2
    i += 1
print(f'Tổng S1 = {S1}')

# b) Tính tổng S2 = (2*1+1)^3 + (2*2+1)^3 + ... + (2*n2+1)^3
n2 = int(input('Nhập n2: '))
while n2 <= 0:
    n2 = int(input('Vui lòng nhập lại n2 (n2 > 0): '))
S2 = 0
i2 = 1
while i2 <= n2:
    S2 += (2 * i2 - 1) ** 3  
    i2 += 1
print(f'Tổng S2 = {S2}')

# c) Tính tổng S3 = (2*1)^4 + (2*2)^4 + ... + (2*n3)^4
n3 = int(input('Nhập n3: '))
while n3 <= 0:
    n3 = int(input('Vui lòng nhập lại n3 (n3 > 0): '))
S3 = 0
i3 = 1
while i3 <= n3:
    S3 += (2 * i3) ** 4  
    i3 += 1
print(f'Tổng S3 = {S3}')

    
    
    