n = int(input("Nhap so phan tu: "))
a = [(int(input(f"Nhap phan tu thu {i + 1}: ")), i) for i in range(n)]
x = int(input("Nhap gia tri x: "))
closest_value, closest_pos = min(a, key=lambda item: abs(item[0] - x))
print("Phan tu gan nhat voi", x, "la", closest_value, "o vi tri", closest_pos)
