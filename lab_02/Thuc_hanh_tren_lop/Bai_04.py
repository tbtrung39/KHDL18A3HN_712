#Câu 4
n = int(input("Nhập vào một số nguyên: "))
n = abs(n)
if n >= 100:
    hang_tram = (n // 100) % 10
else:
    hang_tram = 0
print(f"Chữ số hàng trăm: {hang_tram}")

