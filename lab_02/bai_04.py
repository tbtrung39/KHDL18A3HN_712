#cau4:
so_nguyen = int(input("Nhập vào một số nguyên: "))
if so_nguyen >= 100:
    chu_so_hang_tram = (so_nguyen // 100) % 10
    print("Chữ số hàng trăm là:", chu_so_hang_tram)
else:
    print("0")