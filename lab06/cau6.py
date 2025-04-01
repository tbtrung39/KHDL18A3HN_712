import random
A=[random.randint(1,99999) for i in range(1000)]
A.sort()
print("danh sách sau khi sắp xếp không sử dụng hàm sorted(): ",A)
A=[random.randint(1,99999) for i in range(1000)]
print("danh sách sau khi sắp xếp bằng hàm sorted(): ",sorted(A))