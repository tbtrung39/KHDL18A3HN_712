# câu 9:
a, b, c = map(float,input("xin mời nhập độ dài 3 cạnh: ").split())
chuvi = a + b + c
p = chuvi/2; import math
dientich = math.sqrt(p*(p-a)*(p-b)*(p-c))
print(f" Chu vi tam giác là {chuvi: .2f}")
print(f"Diện tích tam giác là {dientich: .2f}")
