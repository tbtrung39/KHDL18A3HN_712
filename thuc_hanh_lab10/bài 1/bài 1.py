import my_Triange
a = float(input("Nhập cạnh a:"))
b = float(input("Nhập cạnh b:"))
c = float(input("Nhập cạnh c:"))
if my_Triange.is_TamGiac(a, b, c):
    print("Ba cạch tao thành một tam giác")
    print(f"Chu vi hình tam giác: {my_Triange.ChuviTamGiac(a, b, c)}")
    print(f"Diện tích hình tam giác :{my_Triange.S_TamGiac(a, b, c):.2f}")
else:
    print("Ba cạnh không tạo thành hình tam giác")