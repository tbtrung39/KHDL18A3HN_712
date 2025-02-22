so_kw = int(input("Nhập số KW điện tiêu thụ: "))

if so_kw >= 0 and so_kw <= 100:
    tien_dien = so_kw * 2000
    print(so_kw, "x 2000 =", tien_dien, "đồng")
elif so_kw >= 101 and so_kw <= 200:
    tien_dien = so_kw * 2500
    print(so_kw, "x 2500 =", tien_dien, "đồng")
elif so_kw >= 201 and so_kw <= 300:
    tien_dien = so_kw * 3000
    print(so_kw, "x 3000 =", tien_dien, "đồng")
elif so_kw > 300:
    tien_dien = so_kw * 5000
    print(so_kw, "x 5000 =", tien_dien, "đồng")
else:
    print("Số KW không hợp lệ.")