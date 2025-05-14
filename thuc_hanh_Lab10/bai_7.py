import random
import math
def sinh_day_so(n):
    ds = []
    for _ in range(n):
        ds.append(random.randint(1, 100))
    return ds
def liet_ke_chia_het_cho_7(ds):
    return [x for x in ds if x % 7 == 0]
def tong_so_le(ds):
    return sum(x for x in ds if x % 2 != 0)
def la_so_chinh_phuong(n):
    return int(n**0.5) ** 2 == n
def kiem_tra_chinh_phuong(ds):
    return [x for x in ds if la_so_chinh_phuong(x)]
