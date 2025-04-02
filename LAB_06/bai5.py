n = int(input("Nhap so phan tu: "))
a = [(int(input(f"Nhap phan tu thu {i + 1}: ")), i) for i in range(n)]
even_list = [x for x in a if x[0] % 2 == 0]
odd_list = [x for x in a if x[0] % 2 != 0]
even_list.sort(key=lambda x: x[0])
odd_list.sort(key=lambda x: x[0], reverse=True)
sorted_a = []
for value, index in a:
    if value % 2 == 0:
        sorted_a.append(even_list.pop(0)[0])
    else:
        sorted_a.append(odd_list.pop(0)[0])
print("Danh sach sau khi sap xep:", sorted_a)
