r = float(input("nhập bán kính muốn nhập:"))
h = float(input("nhập chiều cao muốn nhập:"))
s_xq = 2*3.14*r*h
s_tp = (2*3.14*r*h) + 2*3.14*r**2
print("giá trị diện tích xung quanh là:",round(s_xq))
print("giá trị diện tich toàn phần là:",round(s_tp))