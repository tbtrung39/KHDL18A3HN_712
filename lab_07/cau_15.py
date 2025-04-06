list1 = list(map(int, input("Nhập danh sách các số (cách nhau bằng khoảng trắng): ").split()))
list2 = input("Nhập danh sách các tên (cách nhau bằng khoảng trắng): ").split()
tu_dien = {list1[i]: list2[i] for i in range(len(list1))}
print(tu_dien)
