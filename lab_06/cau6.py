import random
A=[random.randint(1,99999) for i in range(1000)]
A.sort()
print("danh sach sau khi khong dung ham sorted(): ",A)
A=[random.randint(1,99999) for i in range(1000)]
print("danh sach sau khi dung ham sorted(): ",sorted(A))