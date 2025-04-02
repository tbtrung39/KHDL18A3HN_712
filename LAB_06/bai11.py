n = int(input("Nhap so phan tu: "))
a = [int(input(f"Nhap phan tu thu {i + 1}: ")) for i in range(n)]
unique_list = list(dict.fromkeys(a))
print("Danh sach sau khi xoa phan tu trung nhau:", unique_list)
