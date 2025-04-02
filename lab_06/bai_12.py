danh_sach_giao_dich = ["D 300","D 300","W 200","D 100"]
so_du_ban_dau = 0
for danh_sach_giao_dich in danh_sach_giao_dich:
    parts = danh_sach_giao_dich.split()
    if len(parts) == 2:
        giao_dich,so_luong = parts[0],int(parts[1])
        if giao_dich == "D":
            so_du_ban_dau += so_luong
        elif giao_dich == "W":
            so_du_ban_dau -= so_luong
print(so_du_ban_dau)