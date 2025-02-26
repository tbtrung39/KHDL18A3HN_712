kw = int(input("Nhập số KW điện tiêu thụ: "))
if kw <= 100:
    tien_dien = kw * 2000
elif kw <= 200:
    tien_dien = 100 * 2000 + (kw - 100) * 2500
elif kw <= 300:
    tien_dien = 100 * 2000 + 100 * 2500 + (kw - 200) * 3000
else:
    tien_dien = 100 * 2000 + 100 * 2500 + 100 * 3000 + (kw - 300) * 5000
print(f"Số tiền điện phải trả là: {tien_dien} đồng")
