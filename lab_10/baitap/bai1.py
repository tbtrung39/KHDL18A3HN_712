from pkg import my_Triangle

a, b, c = 3, 4, 5

if my_Triangle.is_TamGiac(a, b, c):
    print("Ba cạnh tạo thành một tam giác.")
    print("Chu vi tam giác là:", my_Triangle.ChuviTamGiac(a, b, c))
    print("Diện tích tam giác là:", my_Triangle.S_TamGiac(a, b, c))
else:
    print("Ba cạnh không tạo thành tam giác.")