# bai 5
# Sinh một dãy list A gồm 1000 số tự nhiên ngẫu nhiên trong khoảng [1, 99999]
A = []
for i in range(1000):
    num = (i * 123456789) % 99999 + 1  
    A.append(num)
print("Danh sách A:", A)
