so_nguyen = int(input("Nhập vào một số nguyên: "))
if so_nguyen >= 100:
    chu_so_hang_tram = (so_nguyen // 100) % 10
else:
    chu_so_hang_tram = 0

print("Chữ số hàng trăm là:", chu_so_hang_tram)