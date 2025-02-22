n = int(input('nhập số lần tung n:'))
p1 = (1/6)**3
p2 = 1 - p1
p3 = (p2)**n
P = 1- p3
print(f"xác suất khi tung n lần 3 xúc xắc có ít nhất 1 lần cả 3 ra 6 là:{round(P,2)}")