num = int(input("Nhập số nguyên: "))
if abs(num) >= 100:
    print(f"Chữ số hàng trăm: {abs(num) // 100 % 10}")
else:
    print("Không có chữ số hàng trăm.")