t = int(input("Nhập thời gian sử dụng (giây): "))
p = (220 * 2.7 * t) / 3600000 * 7000
print("Tiền điện phải trả:", round(p, 2), "VND")