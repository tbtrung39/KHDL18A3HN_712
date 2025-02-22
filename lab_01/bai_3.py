r = float(input("Nhập bán kính khối trụ :"))
h = float(input("nhập chiều cao khối trụ:"))

S_xung_quanh = 2*r*h*3.14
S_toan_phan = 2*3.14*r*h + 2*3.14*r**2
V_khoi_tru = 3.14*r**2*h
print(f"Diện tích xung quanh của khối trụ là: {round(S_xung_quanh,2)}")
print(f"Diện tích toàn phần của khối trụ là : {round(S_toan_phan,2)}")
print(f"Thể tích khối trụ là: {round(V_khoi_tru,2)}")