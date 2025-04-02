#Bai10
import random
ds_so = []
for so in range(0, 201):
    if so % 5 == 0 and so % 7 == 0:
        ds_so.append(so)
random_vtri = random.randint(0, len(ds_so) - 1)
random_so = ds_so[random_vtri]
print("Số ngẫu nhiên được chọn là:",random_so)