import random
import math

def sinh_day_so(so_luong=100):
    return [random.randint(1, 999) for _ in range(so_luong)]

def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def liet_ke_nguyen_to_chia_het_cho_7(day_so):
    return [so for so in day_so if la_so_nguyen_to(so) and so % 7 == 0]

def tinh_tong_so_le(day_so):
    return sum(so for so in day_so if so % 2 != 0)

def la_so_chinh_phuong(n):
    can = int(math.sqrt(n))
    return can * can == n

def kiem_tra_so_chinh_phuong(day_so):
    return [so for so in day_so if la_so_chinh_phuong(so)]
