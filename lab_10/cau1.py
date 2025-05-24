import my_Triangle
a = float(input("hay nhap canh  a: "))
b = float(input("hay nhap canh  b: "))
c = float(input("hay nhap canh c: "))
if my_Triangle.is_TamGiac(a, b, c):
    print("day la mot tam giac.")
    print("Chu vi tam giac la:", my_Triangle.ChuviTamGiac(a, b, c))
    print("s tam giac la:", my_Triangle.S_TamGiac(a, b, c))
else:
    print("Ba canh da nhap ko tao thanh mot tam giac")