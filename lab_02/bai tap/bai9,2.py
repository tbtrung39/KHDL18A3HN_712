kw = int(input("Nhập số KW điện tiêu thụ: "))

if 0 <= kw <= 100:
    gia = 2000
elif 101 <= kw <= 200:
    gia = 2500
elif 201 <= kw <= 300:
    gia = 3000
else:
    gia = 5000

tien_dien = kw * gia
print("Tiền điện phải trả:", tien_dien, "đồng")
