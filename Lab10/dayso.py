import random
import math
def sinh_day_so(n=100):
    return [random.randint(1, 100) for i in range(n)]
def liet_ke_chia_het_cho_7(day):
    return [x for x in day if x % 7 == 0]
def tong_day(day):
    return sum(day)
def co_chinh_phuong(day):
    for so in day:
        can_bac_hai = math.isqrt(so)
        if can_bac_hai * can_bac_hai == so:
            return True
    return False