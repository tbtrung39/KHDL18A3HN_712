n = int(input("Nhap so phan tu: "))
a = [(int(input(f"Nhap phan tu thu {i + 1}: ")), i) for i in range(n)]
positive_list = [x for x in a if x[0] > 0]
negative_list = [x for x in a if x[0] < 0]
positive_list.sort(key=lambda x: x[0])
negative_list.sort(key=lambda x: x[0], reverse=True)
sorted_a = []
for value, index in a:
    if value > 0:
        sorted_a.append(positive_list.pop(0)[0])
    elif value < 0:
        sorted_a.append(negative_list.pop(0)[0])
    else:
        sorted_a.append(0)
print("Danh sach sau khi sap xep:", sorted_a)
