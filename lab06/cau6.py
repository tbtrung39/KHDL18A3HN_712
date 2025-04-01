import random
A=[random.randint(1,99999) for i in range(1000)]
print("Danh sách ban đầu:",A)
#Cách 1 sử dụng hàm sorted
A_sorted=sorted(A)
print("Danh sách sau khi sắp xếp dùng sorted:",A_sorted)
#Cách 2 không dùng sorted
A_khong_sorted=A[:]
n=len(A_khong_sorted)
for i in range(n-1):
    for j in range(n-i-1):
        if A_khong_sorted[j] >A_khong_sorted[j+1]:
            A_khong_sorted[j],A_khong_sorted[j+1]=A_khong_sorted[j+1],A_khong_sorted[j]
print("Danh sách sau khi sắp xếp không dùng sorted:",A_khong_sorted)