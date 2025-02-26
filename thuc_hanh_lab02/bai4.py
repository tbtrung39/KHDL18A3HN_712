num = int(input("Nhập một số nguyên có 3 chữ số: "))
if num < 100 or num > 999:
    print("Số không hợp lệ!")
else:
    hang_tram = num // 100
    print(f"Chữ số hàng trăm của số {num} là {hang_tram}")
