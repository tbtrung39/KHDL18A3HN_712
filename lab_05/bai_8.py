Str = input("Nhap doan van ban: ")
tu_don = input("Nhap tu don can tim: ")
van_ban = Str.split()
so_lan_xuat_hien = 0
for tu in van_ban:
    if tu == tu_don:
        so_lan_xuat_hien += 1
print("So tu don xuat hien trong doan van la:",so_lan_xuat_hien)