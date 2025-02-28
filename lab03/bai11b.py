n = int(input("Nhập số n: "))
for i in range(1, n):
    print(' ' * (n - i), end='')  
    if i > 1:
        print('*' + ' ' * (2 * (i - 1) - 1) + '*')  
    else:
        print('*')  
print('* ' * n)