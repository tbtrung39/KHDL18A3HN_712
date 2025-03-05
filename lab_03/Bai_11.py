# a: 
n= int(input("Nhập số n: "))
chieu_rong = 2 * (n+ 1) - 1
for i in range(n):
    if i == 0:
        hang = '*'
        do_dai_hang = 1
    elif i == n- 1:
        hang = '* ' * (n+ 1)
        do_dai_hang = 2 * (n+ 1) - 1  
    else:
        khoang_trong = 2 * i - 1
        hang = '*' + ' ' * khoang_trong + '*'
        do_dai_hang = 2 + khoang_trong 
    khoang_trang_ben_trai = (chieu_rong - do_dai_hang) // 2
    print(" " * khoang_trang_ben_trai + hang)   
    if i != n- 1:
        print()
print(' ======== a ======== \n')

# b:
for i in range(1, n):
    print(' ' * (n - i), end='')  
    if i > 1:
        print('*' + ' ' * (2 * (i - 1) - 1) + '*')  
    else:
        print('*')  
print('* ' * n)
print(' ======== b ======== \n')
# c:
so_sao_cuoi = n + 1
chieu_rong_max = 2 * so_sao_cuoi - 1
for i in range(n):
    so_sao = i + 1 if i < n - 1 else so_sao_cuoi
    hang_sao = '* ' * so_sao
    khoang_trang = (chieu_rong_max - (2 * so_sao - 1)) // 2
    print(' ' * khoang_trang + hang_sao)
print(' ======== c ======== \n')