n = int(input("Nhap so phan tu: "))
a = [int(input(f"Nhap phan tu thu {i + 1}: ")) for i in range(n)]
unique_list = [x for x in a if a.count(x) == 1]
print("Danh sach chi giu lai cac so xuat hien 1 lan:", unique_list)
