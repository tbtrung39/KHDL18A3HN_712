r = float(input("Nhập bán kính khối trụ: "))
h = float(input("Nhập chiều cao khối trụ: "))
pi = 3.14

dien_tich_xq = 2*pi*r*h
dien_tich_tp = dien_tich_xq + 2*pi*r**2
the_tich = pi*r**2*h

dien_tich_xq = round(dien_tich_xq, 2)
dien_tich_tp = round(dien_tich_tp, 2)
the_tich = round(the_tich, 2)

print(f"Diện tích xung quanh: {dien_tich_xq}")
print(f"Diện tích toàn phần: {dien_tich_tp}")
print(f"Thể tích khối trụ: {the_tich}")
