kw = float(input("Nhập số KW điện tiêu thụ: "))
if 0 <= kw <= 100:
    price_per_kw = 2000
elif 101 <= kw <= 200:
    price_per_kw = 2500
elif 201 <= kw <= 300:
    price_per_kw = 3000
elif kw > 300:
    price_per_kw = 5000
else:
    print("Số KW không hợp lệ.")
    exit()
total_cost = kw * price_per_kw
print(f"Tiền điện phải trả là: {total_cost} đồng.")