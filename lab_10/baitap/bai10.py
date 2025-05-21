from pkg import my_Triangle, my_square

print("Tam giác 3-4-5")
if my_Triangle.is_TamGiac(3, 4, 5):
    print("Chu vi:", my_Triangle.ChuviTamGiac(3, 4, 5))
    print("Diện tích:", my_Triangle.S_TamGiac(3, 4, 5))

print("Hình vuông cạnh 6")
print("Chu vi:", my_square.ChuviHinhvuong(6))
print("Diện tích:", my_square.DientichHinhvuong(6))