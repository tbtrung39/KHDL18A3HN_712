#Bai11
import random
n = int(input("Nhập số phần tử trong danh sách: "))
lst_a = []
for i in range(n):
    j = int(input(f"Nhập phần tử thứ {i+1}: ")) 
    lst_a.append(j) 
print("Danh sách lst_a:", lst_a)
#a.Tạo ra một đánh sách B chứa các phần tử chia hết cho 3 nhưng không chia hết cho 5 từ danh sách A
lst_b = []
for j in lst_a:
    if j % 3 == 0 and j % 5 != 0:
        lst_b.append(j)
print("Danh sách lst_b (chia hết cho 3 nhưng không chia hết cho 5):", lst_b)
#b.Tạo một danh sách C với các phần tử là bình phương của danh sách A
lst_c = []
for j in lst_a:
    lst_c.append(j ** 2)
print("Danh sách lst_c (bình phương của lst_a):", lst_c)
#c.Tạo danh sách D gồm các phần tử lấy ngẫu nhiên từ danh sách A mà chia hết cho 3
lst_d=[]
ds_dk = []
for j in lst_a:
    if j % 3 == 0: 
        ds_dk.append(j)
if ds_dk:
    for x in range(min(len(ds_dk), n)): 
        index = random.randint(0, len(ds_dk) - 1)
        lst_d.append(ds_dk[index]) 
print("Danh sách lst_d (chọn ngẫu nhiên từ lst_a mà không chia hết cho 3):", lst_d)