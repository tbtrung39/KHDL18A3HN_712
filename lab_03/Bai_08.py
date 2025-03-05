n = int(input('Nhập vào số n: '))
if n > 0:
    #a: S1 = 1 + 2 + 3 + … + n = n(n+1)/2.
    S1 = 0
    for i in range(1, n + 1):
        S1 += i
    print(f'S1 = {S1}')

    #b: S2 = 1 + 3 + 5 + … + (2n+1) = (n+1)2
    S2 = (n + 1) ** 2
    print(f'S2 = {S2}')

    #c: # # c) S3 = 2 + 4 + 6 + … + 2n = n(n+1)
    S3 = n * (n + 1)
    print(f'S3 = {S3}')
else:
    print('Số nhập vào không hợp lệ')