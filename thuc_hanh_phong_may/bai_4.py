x = float(input("Nhập giá trị x: "))
bieuthuc = (-x + (x**2 + 4)**0.5) / ((x**4 + 1)**(1/7))
print(f"f({x}) = {round(bieuthuc, 2)}")
