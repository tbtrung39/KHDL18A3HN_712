#cau a
n = int(input("Nhập số n: "))
chieu_rong = 2 * (n + 1) - 1
for i in range(n):
    if i == 0:
        hang = '*'
        do_dai_hang = 1
    elif i == n - 1:
        hang = '* ' * (n + 1)
        do_dai_hang = 2 * (n + 1) - 1  
    else:
        khoang_trong = 2 * i - 1
        hang = '*' + ' ' * khoang_trong + '*'
        do_dai_hang = 2 + khoang_trong 
    khoang_trang_ben_trai = (chieu_rong - do_dai_hang) // 2
    print(" " * khoang_trang_ben_trai + hang)   
    if i != n - 1:
        print()
#cau b
n = int(input("Nhập số n: "))
for i in range(1, n):
    print(' ' * (n - i), end='')  
    if i > 1:
        print('*' + ' ' * (2 * (i - 1) - 1) + '*')  
    else:
        print('*')  
print('* ' * n)
#cau c
n = int(input("Nhập số hàng: "))

for i in range(1, n):
    print(" " * (n - i) + "* " * i)
print("* " * n)