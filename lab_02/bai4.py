n = int(input('Nhập vào số nguyên: '))
if n < 100:
    print(0)
else:
    chu_so_hang_tram = (n // 100) % 10
    print(f' Chữ số hàng trăm của {n} là: ', chu_so_hang_tram)

