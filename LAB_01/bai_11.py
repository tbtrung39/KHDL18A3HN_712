
n = int(input("Nhập số lần tung xúc xắc: "))
p1 = 1 / 216  
p2 = (1 - p1) ** n  
p3= 1 - p2 
ket_qua = round(p3, 2)
print("Xác suất có ít nhất một lần cả ba xúc xắc ra 6 là:", ket_qua)