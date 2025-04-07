l1 = list(map(int, input("Nhập danh sách các số (cách nhau bằng khoảng trắng): ").split()))
l2 = input("Nhập danh sách các tên (cách nhau bằng khoảng trắng): ").split()
td = {l1[i]: l2[i] for i in range(len(l1))}
print(td)