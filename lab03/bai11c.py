so_hang = int(input("Nhập số hàng: "))
so_sao_cuoi = so_hang + 1
chieu_rong_max = 2 * so_sao_cuoi - 1
for i in range(so_hang):
    so_sao = i + 1 if i < so_hang - 1 else so_sao_cuoi
    hang_sao = '* ' * so_sao
    khoang_trang = (chieu_rong_max - (2 * so_sao - 1)) // 2
    print(' ' * khoang_trang + hang_sao)