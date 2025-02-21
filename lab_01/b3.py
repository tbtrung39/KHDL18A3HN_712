# bài 3
r = float(input('nhập bán kính khối trụ :'))
h = float(input('nhập chiều cao khối trụ:'))
pi = 3,14
dtich_xung_quanh = 2*pi*r*h
dtich_toan_phan = 2*pi*r*h + 2*pi*r**2
the_tich_khoi_tru = pi*r**2*h
print(f"diện tích xquanh của khối trụ là: {round(dtich_xung_quanh,2)}")
print(f"diện tích toàn phần của khối trụ là : {round(dtich_toan_phan,2)}")
print(f"thể tích khối trụ là: {round(the_tich_khoi_tru,2)}")
