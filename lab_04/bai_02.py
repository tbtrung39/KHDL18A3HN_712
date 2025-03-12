import math
n = int(input('Nhập số nguyên dương: '))
while n<=0:
    n = int(input('Nhập số nguyên dương: '))

# a)
S = 0
for i in range(1, n+1):
    if i%2 == 0:
        S -= 1/i
    else:
        S += 1/i
print('Tổng của S =',S)

# b)
S = 0
for i in range(2, n+2):
    S += 1/(i*(i-1))
print('Tổng của S =',S)

# c)
S = 0
i = 2
for i in range(2, n+1):
    S += 1/(i**0.5)
    i += 1
print('Tổng của S =',S)