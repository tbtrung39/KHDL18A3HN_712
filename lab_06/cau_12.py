so_du = 0
while True:
    nhap = input("Nhập giao dịch (D/W số tiền) hoặc bấm Enter để kết thúc: ").strip()
    if not nhap:
        break
    phan_tu = nhap.split()
    if len(phan_tu) != 2:
        print("Dữ liệu không hợp lệ, vui lòng nhập lại!")
        continue
    loai_giao_dich, so_tien = phan_tu[0], phan_tu[1]
    if not so_tien.isdigit():
        print("Số tiền không hợp lệ!")
        continue
    so_tien = int(so_tien)
    if loai_giao_dich == "D":
        so_du += so_tien
    elif loai_giao_dich == "W":
        so_du -= so_tien
    else:
        print("Lệnh không hợp lệ, vui lòng nhập lại!")
print("Số dư cuối cùng:", so_du)