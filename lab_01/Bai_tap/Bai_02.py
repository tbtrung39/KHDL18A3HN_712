t = float(input("Nhập số giây: "))
d = t // 86400
h = (t % 86400) // 3600
m = (t % 3600) // 60
s = t % 60
print(f"{int(d)} ngày, {int(h)} giờ, {int(m)} phút, {s:.2f} giây")