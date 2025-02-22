import math
a = float(input("Nhập vận tốc a của xe ô tô: "))

# Tính log4(5)
log4_5 = math.log(5,4)  

# Tính thời gian t
t = (a**4) / log4_5
t = round(t, 2)

print(f"Thời gian ô tô đi được đến lúc dừng là: {t} giây")