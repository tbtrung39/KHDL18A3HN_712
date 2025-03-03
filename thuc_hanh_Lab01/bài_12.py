import math
a = float(input("Nhập vận tốc ban đầu của ô tô (m/s): "))
log4_5 = math.log(5) / math.log(4)  
t = (a ** 4) / log4_5
print(f"Thời gian để ô tô dừng lại là: {t:.2f} giây")
