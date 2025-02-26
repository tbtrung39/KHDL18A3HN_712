so = int(input("Nhập vào một số nguyên: "))
if so >= 100 or so <= -100:
    if so < 0:
        hang_tram = (so // 100) * -1  
    else:
        hang_tram = so // 100
    print(f"Chữ số hàng trăm là: {hang_tram}")
else:
    print("Chữ số hàng trăm là: 0")
