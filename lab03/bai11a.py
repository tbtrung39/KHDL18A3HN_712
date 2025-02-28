so_n = int(input("Nhập số n: "))
chieu_rong = 2 * (so_n + 1) - 1
for i in range(so_n):
    if i == 0:
        hang = '*'
        do_dai_hang = 1
    elif i == so_n - 1:
        hang = '* ' * (so_n + 1)
        do_dai_hang = 2 * (so_n + 1) - 1  
    else:
        khoang_trong = 2 * i - 1
        hang = '*' + ' ' * khoang_trong + '*'
        do_dai_hang = 2 + khoang_trong 
    khoang_trang_ben_trai = (chieu_rong - do_dai_hang) // 2
    print(" " * khoang_trang_ben_trai + hang)   
    if i != so_n - 1:
        print()
