n = int(input("Nhap so phan tu: "))
a = [int(input(f"Nhap phan tu thu {i + 1}: ")) for i in range(n)]
sorted_list = sorted(a)
print("Danh sach sau khi sap xep tang dan:", sorted_list)
