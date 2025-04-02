so_tien = 0
while True:
    giao_dich = input("Nhập giao dịch (nhập 'done' để kết thúc): ")
    if giao_dich == 'done':
        break

    try:
        loai_giao_dich, so_tien_giao_dich = giao_dich.split()
        so_tien_giao_dich = int(so_tien_giao_dich)

        if loai_giao_dich == 'D':
            so_tien += so_tien_giao_dich
        elif loai_giao_dich == 'W':
            so_tien -= so_tien_giao_dich
        else:
            print("Loại giao dịch không hợp lệ.")
    except ValueError:
        print("Định dạng giao dịch không hợp lệ.")

print(so_tien)