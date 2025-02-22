#Bài 12
import math
a = float(input("Nhập vận tốc ban đầu của ô tô: "))
#Tính toán khi xe dùng
#-t*log4(5)+a**4=0
#a**4=t*log(4)5
#t=a**4/log(4)55
gia_tri = math.log(5) / math.log(4)
t = a**4 / gia_tri
t = round(t, 2)
print(f"Thời gian ô tô đi được cho đến lúc dừng: {t} giây")