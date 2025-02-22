# Bài 4
so = int(input("Nhập một số nguyên: "))
if so >= 100 or so <= -100:
    hang_tram = abs(so) // 100 % 10
else:
    hang_tram = 0
print("Chữ số hàng trăm là:", hang_tram)