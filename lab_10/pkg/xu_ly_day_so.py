import random
import math

def sinh_day_so(n=100):
    return [random.randint(1, 500) for _ in range(n)]

def so_nguyen_to_chia_het_7(lst):
    return [x for x in lst if x % 7 == 0 and all(x % i != 0 for i in range(2, int(x**0.5)+1))]

def tong_so_le(lst):
    return sum(x for x in lst if x % 2 != 0)

def la_so_chinh_phuong(n):
    return int(math.sqrt(n)) ** 2 == n

def kiem_tra_chinh_phuong(lst):
    chinh_phuong = [x for x in lst if la_so_chinh_phuong(x)]
    return chinh_phuong if chinh_phuong else None