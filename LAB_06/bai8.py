n = int(input("Nhap so phan tu: "))
a = [(int(input(f"Nhap phan tu thu {i + 1}: ")), i) for i in range(n)]
x = int(input("Nhap gia tri x: "))
last_pos = -1
for value, index in a:
    if value == x:
        last_pos = index
if last_pos != -1:
    print("Vi tri xuat hien cuoi cung cua", x, "la", last_pos)
else:
    print(x, "khong ton tai trong danh sach")
