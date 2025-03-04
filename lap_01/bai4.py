num = int(input("Nhập một số nguyên: "))
if abs(num) >= 100:
    hundreds_digit = abs(num) // 100 % 10
    print(f"Chữ số hàng trăm của số {num} là {hundreds_digit}.")
else:
    print("Chữ số hàng trăm của số này là 0.")