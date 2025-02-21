import math
a = float(input("Nhập vận tốc xe: "))
t = (a**4) / math.log(5, 4)
print("Thời gian dừng:", round(t, 2))