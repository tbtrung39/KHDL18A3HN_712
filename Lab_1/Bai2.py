# Bài 2: 
s=float(input("Nhập số giây:")) 
d = s/86400 
h = d * 24 
m = h * 60 
s = m * 60 
print(f'{s} là {d} ngày, {h} giờ, {m} phút, {s} giây.')