n = int(input("Nhap so phan tu: "))
a = [int(input(f"Nhap phan tu thu {i + 1}: ")) for i in range(n)]
filtered_list = [x for x in a if x % 2 == 0]
print("Danh sach sau khi xoa so le:", filtered_list)
