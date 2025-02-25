num = int(input("Nhập vào một số nguyên: "))

if num < 100:
    print("Chữ số hàng trăm: 0")
else:
    print("Chữ số hàng trăm:", (num // 100) % 10)
