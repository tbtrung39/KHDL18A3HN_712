import math
a = float(input("Nhập vận tốc a: "))
t = (a / 4) / (math.log(5) / math.log(4))
print("Thời gian xe đi đến lúc dừng:", round(t, 2))
