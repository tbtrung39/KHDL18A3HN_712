a1, a2, a3 = map(int, input("Nhập vector a (cách nhau bởi dấu cách): ").split())
b1, b2, b3 = map(int, input("Nhập vector b (cách nhau bởi dấu cách): ").split())
tich_vo_huong = a1*b1 + a2*b2 + a3*b3
print("Tích vô hướng của hai vector:", tich_vo_huong)