# bài 9
so_kw = int(input("Nhập số KW điện tiêu thụ: "))
if 0 <= so_kw <= 100:
    tien_dien=so_kw*2000
elif 101 <= so_kw <= 200:
    tien_dien = so_kw*2500
elif 201 <= so_kw <= 300:
    tien_dien = so_kw*3000
elif so_kw > 300:
    tien_dien=so_kw*50005000
print("Tiền điện phải trả là:", tien_dien, "đồng")
