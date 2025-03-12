n = int(input("Nhập vào một số nguyên: "))

# Lấy chữ số hàng trăm bằng cách chia số cho 100 và lấy phần nguyên
so_hang_tram = abs(n) // 100 % 10  

if abs(n) < 100:
    print("Chữ số hàng trăm là: 0")
else:
    print("Chữ số hàng trăm là: ", so_hang_tram)