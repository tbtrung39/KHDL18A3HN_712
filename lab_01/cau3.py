r=int(input("nhập vào bán kính r: "))
h=int(input("nhập vào chiều cao hình trụ: "))
pi=3.14
dt_xq=2*pi*r*h
dt_tp=dt_xq + 2*pi*(r**2)
the_tich=2*pi*(r**2)*h
print("diện tích xung quanh của khối trụ là: ",dt_xq )
print("diện tích toàn phần của khối trụ là: ",dt_tp)
print("thể tích của khối trụ là: ",the_tich)