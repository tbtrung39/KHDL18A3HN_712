a = float(input("Nhập giá trị a: "))
b = float(input("Nhập giá trị b: "))
c = float(input("Nhập giá trị c: "))

if a == 0:
    print("Đây không phải là phương trình bậc 2.")
else:
    x_dinh = -b/(2*a)
    D = b**2 - 4*a*c
    y_dinh = -D/(4*a)
    
    x_dinh = round(x_dinh, 2)
    y_dinh = round(y_dinh, 2)
    
    print(f"Tọa độ đỉnh của phương trình bậc 2 là: (x, y) = ({x_dinh}, {y_dinh})")