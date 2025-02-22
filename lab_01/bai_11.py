n = int(input('nhập số lần tung n:'))
#Tính xsuat để cả 3 xúc xắc cùng ra 6 trong một lần tung là 
p1 = (1/6)**3
#Tính xs để không có lần nào cả 3 cùng ra 6 trong 1 lần tung là
p2 = 1 - p1
#Tính xs để không có lần nào cả 3 cùng ra 6 trong n lần tung là 
p3 = (p2)**n
#Tính xs để có ít nhất 1 lần cả 3 ra 6 trong n lần tung là 
P = 1- p3
print(f"xác suất khi tung n lần 3 xúc xắc có ít nhất 1 lần cả 3 ra 6 là:{round(P,2)}")