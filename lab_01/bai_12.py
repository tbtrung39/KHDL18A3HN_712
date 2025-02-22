import math
a = float(input("Nhập vận tốc ban đầu của ô tô: "))
t_dung = (a**4) * (math.log(4) / math.log(5)) 
t_dung = round(t_dung, 2)
print("Thời gian ô tô đi cho đến khi dừng lại:", t_dung, "giây")