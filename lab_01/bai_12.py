import math
a = float(input("Nhập vận tốc ban đầu của ô tô: "))
t = (a**4) * (math.log(4) / math.log(5)) # thời gian đến khi xe dừng hẳn
t = round(t, 2) # làm tròn 
print("Thời gian ô tô đi cho đến khi dừng lại:", t, "giây")
