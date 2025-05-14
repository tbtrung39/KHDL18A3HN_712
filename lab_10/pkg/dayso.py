import random
import math
def tao_day(n):
    return [random.randint(1,100) for i in range(n)]

def so_chia_het_cho_7(day):
    return [x for x in day if x%7 == 0]

def tong_so_le(day):
    return sum(x for x in day if x%2 == 1)

def so_chinh_phuong(x):
    return int(math.sqrt(x))**2 == x

def cac_so_chinh_phuong(day):
    return [x for x in day if so_chinh_phuong(x)]