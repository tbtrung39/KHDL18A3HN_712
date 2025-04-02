#Bai6
import random
list_a = []
for i in range(1000):
    so = random.randint(1, 99999)
    list_a.append(so)
print("Danh sách ban đầu: ", list_a[:20])
# a.Sử dụng sorted()
tang_dan = sorted(list_a)
print(Danh sách tăng dần có dùng sorted():", tang_dan[:20])
# b. Khong su dung sorted()
n = len(list_a)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if list_a[j] > list_a[j + 1]:  
            list_a[j], list_a[j + 1] = list_a[j + 1], list_a[j] 
print("Danh sách tăng dần không dùng  sorted():", list_a[:20])