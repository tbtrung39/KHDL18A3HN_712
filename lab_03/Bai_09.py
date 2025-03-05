# a) S4 = 12 + 22 + 32 + … + n2
n = int(input('Nhập vào số n: '))
if n > 0:
    S4 = 0
    for i in range(1, n + 1):
        S4 += i ** 2
    print(f'S4 = {S4}')

# b) S5 = 13 + 33 + 53 + … + (2n+1)3
    S5 = 0
    for i in range(1, 2 * n + 2, 2):
        S5 += i ** 3
    print(f'S5 = {S5}')

# c) S6 = 24 + 44 + 64 + … + (2n)4
    S6 = 0
    for i in range(2, 2 * n + 1, 2):
        S6 += i ** 4
    print(f'S6 = {S6}')
else:
    print('Số nhập vào không hợp lệ')