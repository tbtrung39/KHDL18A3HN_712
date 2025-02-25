a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))
if a + b > c and b + c > a and c + a > b:
    if a == b == c:
        print("Đây là tam giác đều.")
    elif a == b or b == c or c == a:
        print("Đây là tam giác cân.")
    elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
        if a == b or b == c or c == a:
            print("Đây là tam giác vuông cân.")
        else:
            print("Đây là tam giác vuông.")
else:
    print("Ba số này không phải là ba cạnh của một tam giác.")
