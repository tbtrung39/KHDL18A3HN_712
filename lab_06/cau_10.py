import random

danh_sach = [x for x in range(201) if x % 5 == 0 and x % 7 == 0]
so = random.randint(0, len(danh_sach) - 1)
so_ngau_nhien = danh_sach[so]
print("Số ngẫu nhiên chia hết cho 5 và 7:", so_ngau_nhien)