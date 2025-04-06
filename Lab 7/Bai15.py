#Bai15
n = int(input("Nhập số phần tử của danh sách: "))
list1 = []
for i in range(n):
    m = int(input("Nhập phần tử thứ", i+1, "của list1: "))
    list1.append(m)
list2 = []
for i in range(n):
    ten = input("Nhập tên thứ", i+1, "của list2: ")
    list2.append(ten)
tu_dien = {}
for i in range(n):
    tu_dien[list1[i]] = list2[i]
print(tu_dien)