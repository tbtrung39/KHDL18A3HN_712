import my_Triangle
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))
if my_Triangle.la_tam_giac(a, b, c):
    print("Là tam giác.")
    print("Chu vi:", my_Triangle.ChuviTamGiac(a, b, c))
    print("Diện tích:", my_Triangle.S_TamGiac(a, b, c))
else:
    print("Ba cạnh không tạo thành tam giác.")

