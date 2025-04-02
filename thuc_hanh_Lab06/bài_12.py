giao_dichs = []
while True:
    giao_dich = input("Nhập giao dịch (nhập 'done' để kết thúc): ")
    if giao_dich.lower() == 'done':
        break
    try:
        loai_giao_dich, so_tien_giao_dich = giao_dich.split()
        so_tien_giao_dich = int(so_tien_giao_dich)
        giao_dichs.append((loai_giao_dich.upper(), so_tien_giao_dich))
    except ValueError:
        print("Định dạng giao dịch không hợp lệ.")
so_tien = 0
for loai, tien in giao_dichs:
    if loai == 'D':
        so_tien += tien
    elif loai == 'W':
        so_tien -= tien
print("Số tiền thực trong tài khoản:", so_tien)