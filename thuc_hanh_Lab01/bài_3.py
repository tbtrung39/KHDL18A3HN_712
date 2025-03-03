pi = 3.14
r = float(input("bán kính đáy: "))
h = float(input("chiều cao (h): "))
S_xq = 2 * pi * r * h  
print(f"Diện tích xung quanh: {S_xq:.2f}")
S_tp = S_xq + 2 * pi * r**2  
print(f"Diện tích toàn phần: {S_tp:.2f}")
V = pi * r**2 * h 
print(f"Thể tích khối trụ: {V:.2f}")
