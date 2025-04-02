import random
ds = []
for i in range(1000):
    so = random.randint(1, 99999)
    ds.append(so)

print("20 số đầu tiên trong danh sách ban đầu:", ds[:20])
# Cách 1: Sử dụng hàm sorted()
ds_1 = sorted(ds)
print("\n20 số đầu tiên sau khi sắp xếp bằng sorted():", ds_1[:20])

# Cách 2: Sắp xếp thủ công (Bubble Sort)
ds_2 = ds.copy()
n = len(ds_2)
for i in range(n):
    for j in range(n - 1):
        if ds_2[j] > ds_2[j + 1]:
            ds_2[j], ds_2[j + 1] = ds_2[j + 1], ds_2[j]
print("\n20 số đầu tiên sau khi sắp xếp thủ công:", ds_2[:20])
