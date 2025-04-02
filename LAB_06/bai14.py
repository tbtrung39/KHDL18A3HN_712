n = int(input("Nhap so phan tu: "))
a = [int(input(f"Nhap phan tu thu {i + 1}: ")) for i in range(n)]
sorted_list = sorted(a, reverse=True)
print("Danh sach sau khi sap xep giam dan:", sorted_list)
